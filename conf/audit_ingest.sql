INSERT INTO staging.audit_ingestion
(source_id, source_name, source_date, source_type, source_row_count,
target_name, target_date, target_type, target_row_count, insert_dttm)
VALUES
('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}',
CURRENT_TIMESTAMP)