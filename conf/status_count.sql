select
    case
        when source_row_count = target_row_count
        then 1
        else 0
    end as res
from staging.audit_ingestion
where
    cast(insert_dttm as date) = current_date()
    and source_id = '{0}'