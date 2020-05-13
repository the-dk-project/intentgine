create table prod.delivered_leads (
	id int not null primary key auto_increment,
    campaign varchar(250),
	email varchar(250),
    first_name varchar(250),
    last_name varchar(250),
    phone varchar(250),
    country varchar(250),
    title varchar(250),
    company varchar(250),
    industry varchar(250),
    job_function varchar(250),
    client varchar(250),
    delivery_date date,
    insert_dttm timestamp NOT NULL DEFAULT current_timestamp,
    update_dttm timestamp NOT NULL DEFAULT current_timestamp ON UPDATE current_timestamp
)