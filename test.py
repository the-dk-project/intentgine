from func import db
import os

dir_id = db.load_directory("columns")

for i in dir_id['first_names']:
    print(i)
