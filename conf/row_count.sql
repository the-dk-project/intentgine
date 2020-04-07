select
    count(1)
from dev.delivered_leads_tci
where
    cast(insert_dttm as date) = current_date()
    and campaign = '{0}'