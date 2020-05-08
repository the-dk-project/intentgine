from func import db, gdrive
import pandas as pd

first_names = ['First Name', 'first_name', 'first name', 'FirstName', 'first', 'FName']
last_names = ['Last Name', 'last_name', 'last name', 'LastName', 'last', 'LName']
emails = ['Company Email', 'email', 'company_email', 'Email', 'Work Email', 'Email1']
phones = ['Phone', 'phone', 'Phone1']
countries = ['Country', 'Country Code', 'country']
companies = ['Company Name', 'company', 'Company']
titles = ['Title', 'title', 'Job Title']
industries = ['Industry', 'industry']
job_functions = ['Job Function', 'job_function']
master_list = {'first_name': first_names, 'last_name': last_names, 'email': emails, 'phone': phones, 'country': countries, 'company': companies, 'title': titles, 'industry': industries, 'job_function': job_functions}
delivered_leads = dict()

cxn = db.db_connect("local_mysql")
g_auth = gdrive.google_auth()
intent_macro = '1bSP_i6b542eMBC_kiDxeLHjIFUKzzA_C'
yesterday = '2020-05-06'

def build_columns(df, col_list):
    col = ''
    for element in col_list:
        if element in df.columns:
            col = element
    
    return col

raw_files = gdrive.list_files(g_auth, intent_macro, yesterday)

for raw_file in raw_files:
    gdrive.dl_file_name(g_auth, intent_macro, raw_file)
    df = pd.DataFrame()
    if ".csv" in raw_file:
        df = pd.read_csv(raw_file)
    else:
        df = pd.read_excel(raw_file)

    for k, v in master_list.items():
        col = build_columns(df, v)
        if col == '':
            delivered_leads[k] = col
        else:
            delivered_leads[k] = df[col]
        delivered_leads['client'] = 'IMR'
        delivered_leads['delivery_date'] = yesterday
