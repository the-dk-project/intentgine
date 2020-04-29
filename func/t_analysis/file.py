import os
import xlsxwriter
from datetime import datetime

def file_to_str(directory, file_name):
    file = directory + file_name
    string = open(file, 'r').read()

    return string

def check_file(input_file):
    status = os.path.isfile(input_file)
    if status is False:
        print(datetime.now(), "ERROR: {} missing.".format(input_file))
        exit(1)

def pdf_report(output_path, data, info, title):
    file_name = str(title).split('.')
    workbook = xlsxwriter.Workbook(output_path + file_name[0] + ".xlsx")
    worksheet = workbook.add_worksheet("Sheet1")
    w2 = workbook.add_worksheet("Sheet2")

    row = 0
    col = 0
    sorted_dict = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}
    for k, v in sorted_dict.items():
        key = str(k)
        if len(key) != 1:
            worksheet.write(row, col, k)
            worksheet.write(row, col+1, v)
            row += 1

    i_row = 0
    i_col = 0
    for k, v in info.items():
        w2.write(i_row, i_col, str(k))
        w2.write(i_row, i_col+1, str(v))
        i_row += 1
    
    workbook.close()
