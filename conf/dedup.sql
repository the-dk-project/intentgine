DELETE t1 FROM prod.delivered_leads t1
INNER JOIN prod.delivered_leads t2
WHERE
    t1.campaign = '{0}' AND
    t1.update_dttm < t2.update_dttm AND
    t1.email = t2.email AND
    t1.campaign = t2.campaign;