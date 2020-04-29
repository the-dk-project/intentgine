import pandas as pd


def tci_dataframe(data_list):
    df = pd.DataFrame()
    for i in data_list:
        data_df = pd.DataFrame({'landing_page': i.landing_page, 'campaign': i.campaign, 'first_name': i.first_name, 'last_name': i.last_name, 'title': i.title, 'company': i.company, 'email': i.email, 'phone': i.phone, 'street': i.street, 'city': i.city, 'state_province': i.state_province, 'zip_postal_code': i.zip_postal_code, 'company_size': i.company_size, 'country': i.country, 'industry': i.industry, 'region': i.region, 'job_function': i.job_function, 'title_category': i.title_category, 'technology_interest': i.technology_interest, 'technology_installed': i.technology_installed, 'comments': i.comments, 'duns': i.duns, 'web_address': i.web_address, 'revenue': i.revenue, 'linkedin': i.linkedin, 'selected_docs': i.selected_docs, 'client_name': i.client_name, 'delivery_date': i.delivery_date}, index=[0])
        df = df.append(data_df, ignore_index=True)

    return df


def bwr_dataframe(data_list):
    df = pd.DataFrame()
    for i in data_list:
        data_df = pd.DataFrame({'first_name': i.first_name, 'last_name': i.last_name, 'title': i.title, 'company': i.company, 'email': i.email, 'phone': i.phone, 'street': i.street, 'city': i.city, 'country': i.country, 'zip_postal_code': i.postcode, 'company_size': i.company_size, 'industry': i.industry, 'job_function': i.title, 'linkedin': i.linkedin, 'client_name': i.client_name, 'delivery_date': i.delivery_date}, index=[0])
        df = df.append(data_df, ignore_index=True)

    return df


def qa_dataframe(data_list):
    df = pd.DataFrame()
    for i in data_list:
        data_df = pd.DataFrame({'email': i.email, 'status': i.status, 'qa_status': i.qa_status, 'campaign_id': i.campaign_id, 'qa_name': i.qa_name, 'type': i.type, 'last_sent_date': i.last_sent_date, 'last_open_date': i.last_open_date, 'last_lead_date': i.last_lead_date, 'domain': i.domain, 'sic_code': i.sic_code, 'company_name': i.company_name, 'company_size': i.company_size, 'acc_naisc_code': i.acc_naisc_code, 'industry': i.industry, 'sub_industry': i.sub_industry, 'company_linkedin_url': i.company_linkedin_url, 'first_name': i.first_name, 'last_name': i.last_name, 'title': i.title, 'phone_work': i.phone_work, 'street': i.street, 'city': i.city, 'state': i.state, 'postal_code': i.postal_code, 'country': i.country, 'job_level': i.job_level, 'job_function1': i.job_function1, 'contact_link': i.contact_link, 'job_function2': i.job_function2, 'job_function3': i.job_function3, 'email_status': i.email_status, 'ip': i.ip, 'timestamp': i.timestamp, 'campaign_name': i.campaign_name, 'asset': i.asset, 'asset_link': i.asset_link, 'comments': i.comments, 'facebook': i.facebook, 'twitter': i.twitter, 'timezone': i.timezone, 'brand_domain': i.brand_domain, 'rpc': i.rpc, 'qa_date': i.qa_date}, index=[0])
        df = df.append(data_df, ignore_index=True)

    return df


def hub_dataframe(data_list):
    df = pd.DataFrame()
    for i in data_list:
        data_df = pd.DataFrame({'reject_type': i.status, 'email': i.email, 'delivery_date': i.delivery_date, 'email_status': i.email_status, 'campaign_name': i.campaign_name, 'brand_domain': i.brand_domain, 'ip_address': i.ip}, index=[0])
        df = df.append(data_df, ignore_index=True)

    return df

def sent_dataframe(data_list):
    df = pd.DataFrame()
    for i in data_list:
        data_df = pd.DataFrame({'email': i.email, 'ip': i.ip, 'email_status': i.email_status, 'type': i.type, 'campaign_name': i.campaign_name, 'timestamp': i.timestamp, 'asset': i.asset, 'asset_link': i.asset_link, 'last_sent_date': i.ocx_unsubscribe_date, 'brand_domain': i.brand_domain, 'client_name': i.client_name}, index=[0])
        df = df.append(data_df, ignore_index=True)

    return df
