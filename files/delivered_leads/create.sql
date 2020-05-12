create table prod.delivered_leads (
    email varchar(250) NOT NULL PRIMARY KEY,
    first_name varchar(250),
    last_name varchar(250),
    phone varchar(250),
    country varchar(250),
    title varchar(250),
    company varchar(250),
    industry varchar(250),
    job_function varchar(250),
    client varchar(20),
    delivery_date date,
    insert_dttm timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    update_dttm timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)