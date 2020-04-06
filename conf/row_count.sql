select
    count(1)
<<<<<<< HEAD
from prod.delivered_leads
=======
from dev.delivered_leads_tci
>>>>>>> f6e06a00d41676a79928e3ee3af77e29b919a766
where
    cast(insert_dttm as date) = current_date()
    and campaign = '{0}'