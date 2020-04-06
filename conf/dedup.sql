<<<<<<< HEAD
DELETE t1 FROM prod.delivered_leads t1
INNER JOIN prod.delivered_leads t2
=======
DELETE t1 FROM dev.delivered_leads_tci t1
INNER JOIN dev.delivered_leads_tci t2
>>>>>>> f6e06a00d41676a79928e3ee3af77e29b919a766
WHERE
    t1.campaign = '{0}' AND
    t1.update_dttm < t2.update_dttm AND
    t1.email = t2.email AND
    t1.campaign = t2.campaign;