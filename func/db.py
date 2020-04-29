from configparser import ConfigParser
from sqlalchemy import create_engine
import os


def db_config(conf, section):
    parser = ConfigParser()
    parser.read(conf)

    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, conf))

    return db

def db_connect(section):
    db_conf = os.getcwd().replace("test", "conf") + "\\files\\conf\\" + "db_config.ini"
    db_param = db_config(db_conf, section)
    connection_str = "mysql+pymysql://{0}:{1}@{2}/{3}".format(
        db_param['user'], db_param['password'], db_param['host'], db_param['database']
        )
    engine = create_engine(connection_str)
    cxn = engine.connect()

    return cxn
