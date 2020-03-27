select
    count(1)
from dev.delivered_leads
where
    cast(insert_dttm as date) = current_date()
    and campaign = '{0}'