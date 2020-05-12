from func import db, gdrive
from func.t_analysis import file
import pandas as pd
import os

first_names = ['First Name', 'first_name', 'first name', 'FirstName', 'first', 'FName']
last_names = ['Last Name', 'last_name', 'last name', 'LastName', 'last', 'LName']
emails = ['Company Email', 'email', 'company_email', 'Email', 'Work Email', 'Email1']
phones = ['Phone', 'phone', 'Phone1']
countries = ['Country', 'Country Code', 'country']
companies = ['Company Name', 'company', 'Company']
titles = ['Title', 'title', 'Job Title']
industries = ['Industry', 'industry']
job_functions = ['Job Function', 'job_function', 'Job Department']
master_list = {'first_name': first_names, 'last_name': last_names, 'email': emails, 'phone': phones, 'country': countries, 'company': companies, 'title': titles, 'industry': industries, 'job_function': job_functions}

cxn = db.db_connect("local_mysql")
dir_id = db.load_directory()
g_auth = gdrive.google_auth()
conf_dir = os.getcwd() + "//files//"
intent_macro = '1bSP_i6b542eMBC_kiDxeLHjIFUKzzA_C'
yesterday = '2020-05-08'

def build_columns(df, col_list):
    col = ''
    for element in col_list:
        if element in df.columns:
            col = element
    
    return col

raw_files = gdrive.list_files(g_auth, dir_id['imr'], yesterday)

for raw_file in raw_files:
    gdrive.dl_file_name(g_auth, intent_macro, raw_file)
    dl = dict()
    data = dict()
    df = pd.DataFrame()
    if ".csv" in raw_file:
        df = pd.read_csv(raw_file)
    else:
        df = pd.read_excel(raw_file)

    # Build columns
    for k, v in master_list.items():
        col = build_columns(df, v)
        dl[k] = col
        
    # Build dict
    for index, row in df.iterrows():
        for k, v in dl.items():
            if v == '':
                data[k] = ''
            else:
                data[k] = row[v]
            data['client'] = 'IMR'
            data['delivery_date'] = yesterday

        query = file.file_to_str(conf_dir, 'delivered_leads//insert.sql')
        cxn.execute(query.format(data['email'], data['first_name'], data['last_name'], data['phone'], data['country'], data['title'], data['company'], data['industry'], data['job_function'], data['client'], data['delivery_date']))

    os.remove(raw_file)