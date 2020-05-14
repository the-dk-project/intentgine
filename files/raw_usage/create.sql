CREATE TABLE raw_leads (
  id SERIAL,
  email varchar(250) DEFAULT NULL,
  hygiene_tool_result varchar(50) DEFAULT NULL,
  campaign varchar(250) DEFAULT NULL,
  status varchar(20) DEFAULT NULL,
  insert_dttm timestamp NULL DEFAULT NOW(),
  update_dttm timestamp NULL DEFAULT NOW()
)