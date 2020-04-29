from func.t_analysis import file
from func import db
from datetime import datetime
import os

def audit(data, target_name, target_type):
    cxn = db.db_connect("local_mysql")
    conf_dir = 'd:/project/files/'

    dedup = file.file_to_str(conf_dir, 'tci/dedup.sql')
    row_count = file.file_to_str(conf_dir, 'tci/row_count.sql')
    audit_ingest = file.file_to_str(conf_dir, 'audit/audit_ingest.sql')
    status_count = file.file_to_str(conf_dir, 'audit/status_count.sql')
    status_update = file.file_to_str(conf_dir, 'audit/status_update.sql')

    for key in data.keys():
        current_datetime = datetime.now()
        print("Processing: '{0}' || {1} Rows || {2}".format(data[key]['campaign'], data[key]['count'], data[key]['source_id']))

        # Make generic
        cxn.execute(dedup)

        count_cursor = cxn.execute(row_count.format(data[key]['campaign']))
        result = count_cursor.fetchall()
        tgt_row_count = result[0][0]

        cxn.execute(audit_ingest.format(key, data[key]['file_name'], data[key]['date'], data[key]['type'],
                                        data[key]['count'], target_name, current_datetime, target_type,
                                        tgt_row_count))

        status_cursor = cxn.execute(status_count.format(key))
        result = status_cursor.fetchall()
        status = result[0][0]

        cxn.execute(status_update.format(status, key))

def err_status():
    cxn = db.db_connect("local_mysql")
    status_cursor = cxn.execute("select source_name from staging.audit_ingestion where status = 0")
    result = status_cursor.fetchall()
    
    return result
