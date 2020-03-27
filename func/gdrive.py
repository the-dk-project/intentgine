from oauth2client.service_account import ServiceAccountCredentials
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from datetime import datetime, timedelta
from func import db, audit, notif
import pandas as pd
import gspread
import os


def google_auth():
    g_auth = GoogleAuth()
    g_auth.LocalWebserverAuth()
    g_drive = GoogleDrive(g_auth)

    return g_drive


def spreadsheet(file):
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet_reader.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open(str(file)).sheet1
    result = sheet.get_all_records()

    return result


def excel_to_list(excel_file, sheet, class_name):
    df_source = pd.read_excel(excel_file, sheet_name=sheet)
    data = df_source.values.tolist()
    if excel_file:
        os.remove(excel_file)
    data_list = []

    for d in data:
        data_list.append(class_name(*d))

    return data_list


def list_to_db(data_list, schema, target_table, method, mode='append'):
    cxn = db.db_connect("local_mysql")
    df = method(data_list)

    df.to_sql(con=cxn, name=target_table, schema=schema, if_exists=mode, index=False)

    return df


def process_ingestion(directory_id, process_date, schema, target_name, target_type, class_name, method, sheet):
    g_drive = google_auth()

    file_list = g_drive.ListFile({'q': "'{}' in parents and trashed=false".format(directory_id)}).GetList()
    for file in sorted(file_list, key=lambda x: x['title']):

        key = str(file['id'])
        title = str(file['title'])
        campaign = title.split('}')[0].replace('{', '')
        modified_date_ts = datetime.strptime(file['modifiedDate'], '%Y-%m-%dT%H:%M:%S.%fZ') + timedelta(hours=8)
        modified_datetime = modified_date_ts.strftime('%Y-%m-%d %H:%M:%S.%f')
        #modified_date = modified_date_ts.strftime('%Y-%m-%d')
        modified_date = modified_date_ts.strftime('%Y-%m')

        if str(modified_date) == str(process_date):

            print('Downloading {} from GDrive.'.format(title))
            file.GetContentFile(title)
            try:
                data_list = excel_to_list(title, sheet, class_name)
                dataframe = list_to_db(data_list, schema, target_name, method)
                count = len(dataframe) or 0

                tmp = {key: {'file_name': title, 'campaign': campaign, 'type': file['fileExtension'],
                            'date': str(modified_datetime), 'count': count, 'source_id': key}}
                audit.audit(tmp, target_name, target_type)
            except Exception as e:
                print(e)
                notif.ingestion_mail(title)
                pass

def dl_file_name(directory_id, file_name):
    g_drive = google_auth()

    file_list = g_drive.ListFile({'q': "'{}' in parents and trashed=false".format(directory_id)}).GetList()
    for file in sorted(file_list, key=lambda x: x['title']):
        title = str(file['title'])

        if title == file_name:
            print('Downloading {} from GDrive.'.format(title))
            file.GetContentFile(title)
