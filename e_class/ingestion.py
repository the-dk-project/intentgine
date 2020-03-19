from datetime import date, timedelta


class TCI(object):

    def __init__(self, landing_page, campaign, first_name, last_name, title, company, email, phone, street, city, state_province, zip_postal_code, company_size, country, industry, region, job_function, title_category, technology_interest, technology_installed, comments, duns, web_address, revenue, linkedin, selected_docs, *args):
        self.landing_page = landing_page
        self.campaign = campaign
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.company = company
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state_province = state_province
        self.zip_postal_code = zip_postal_code
        self.company_size = company_size
        self.country = country
        self.industry = industry
        self.region = region
        self.job_function = job_function
        self.title_category = title_category
        self.technology_interest = technology_interest
        self.technology_installed = technology_installed
        self.comments = comments
        self.duns = duns
        self.web_address = web_address
        self.revenue = revenue
        self.linkedin = linkedin
        self.selected_docs = selected_docs
        self.client_name = 'TCI'
        self.delivery_date = str(date.today() - timedelta(days=1))


class SiteCore(object):

    def __init__(self, email, first_name, last_name, street, city, country, postcode, telephone, timestamp_1, company_name, job_title, industry, asset_title, comments, lead_creation_date, sub_source, tactic, company_size, country_lead, lead_type, supplier_lead_id, caller_name, timestamp_2, linkedin, call_recording_link, department, function, script_id, dial_attemps):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.city = city
        self.country = country
        self.postcode = postcode
        self.phone = telephone
        self.timestamp = timestamp_1
        self.company = company_name
        self.title = job_title
        self.industry = industry
        self.asset_title = asset_title
        self.comments = comments
        self.lead_creation_date = lead_creation_date
        self.sub_source = sub_source
        self.tactic = tactic
        self.company_size = company_size
        self.country_lead = country_lead
        self.lead_type = lead_type
        self.supplier_lead_id = supplier_lead_id
        self.caller_name = caller_name
        self.timestamp = timestamp_2
        self.linkedin = linkedin
        self.call_recording_link = call_recording_link
        self.department = department
        self.function = function
        self.script_id = script_id
        self.dial_attemps = dial_attemps
        self.client_name = 'BWR'
        self.delivery_date = str(date.today() - timedelta(days=1))


class QA(object):

    def __init__(self, email, status, qa_status, campaign_id, qa_name, type, last_sent_date, last_open_date, last_lead_date, domain, sic_code, company_name, company_size, acc_naisc_code, industry, sub_industry, company_linkedin_url, first_name, last_name, title, phone_work, street, city, state, postal_code, country, job_level, job_function1, contact_link, job_function2, job_function3, email_status, ip, timestamp, campaign_name, asset, asset_link, comments, facebook, twitter, timezone, brand_domain, rpc, qa_date, *args):
        self.email = email
        self.status = status
        self.qa_status = qa_status
        self.campaign_id = campaign_id
        self.qa_name = qa_name
        self.type = type
        self.last_sent_date = last_sent_date
        self.last_open_date = last_open_date
        self.last_lead_date = last_lead_date
        self.domain = domain
        self.sic_code = sic_code
        self.company_name = company_name
        self.company_size = company_size
        self.acc_naisc_code = acc_naisc_code
        self.industry = industry
        self.sub_industry = sub_industry
        self.company_linkedin_url = company_linkedin_url
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.phone_work = phone_work
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.job_level = job_level
        self.job_function1 = job_function1
        self.contact_link = contact_link
        self.job_function2 = job_function2
        self.job_function3 = job_function3
        self.email_status = email_status
        self.ip = ip
        self.timestamp = timestamp
        self.campaign_name = campaign_name
        self.asset = asset
        self.asset_link = asset_link
        self.comments = comments
        self.facebook = facebook
        self.twitter = twitter
        self.timezone = timezone
        self.brand_domain = brand_domain
        self.rpc = rpc
        self.qa_date = qa_date
        self.delivery_date = str(date.today() - timedelta(days=1))

class HUB(object):

    def __init__(self, email, status, type, ip, timestamp, campaign_name, asset, asset_link, brand_domain, last_sent_date, email_status, *args):
        self.email = email
        self.status = status
        self.type = type
        self.ip = ip
        self.timestamp = timestamp
        self.campaign_name = campaign_name
        self.asset = asset
        self.asset_link = asset_link
        self.brand_domain = brand_domain
        self.last_sent_date = last_sent_date
        self.email_status = email_status
        self.delivery_date = str(date.today() - timedelta(days=1))


class SENT(object):

    def __init__(self, email, status, type, ip, timestamp, campaign_name, asset, asset_link, brand_domain, ocx_unsubscribe_date, email_status, *args):
        self.email = email
        self.status = status
        self.type = type
        self.ip = ip
        self.timestamp = timestamp
        self.campaign_name = campaign_name
        self.asset = asset
        self.asset_link = asset_link
        self.brand_domain = brand_domain
        self.ocx_unsubscribe_date = ocx_unsubscribe_date
        self.email_status = email_status
        self.client_name = 'EXT'
        self.delivery_date = str(date.today() - timedelta(days=1))
