from func import cleaner
from urllib.parse import urlparse
import xlsxwriter
import xlrd

def excel_writer(input_file, output_file, industry, campaign_name, internal_id, external_id):
    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    worksheet.write(row, col, 'Account Name')
    worksheet.write(row, col+1, 'Domain')
    worksheet.write(row, col+2, 'Industry')
    worksheet.write(row, col+3, 'Campaign Name')
    worksheet.write(row, col+4, 'Internal ID')
    worksheet.write(row, col+5, 'External ID')
    worksheet.write(row, col+6, 'Valid')

    wb = xlrd.open_workbook(input_file)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        if i != 0:
            acct_name = sheet.cell_value(i, col)
            url = sheet.cell_value(i, col+1)
<<<<<<< HEAD
            url = cleaner.domain_url(str(url))
=======
            url = cleaner.domain_url(url)
>>>>>>> 78337c77dba0767c4168c30fd4f1e3e7585cd5b7
            domain = url.split('/')[0]

            worksheet.write(i, col, acct_name)
            worksheet.write(i, col+1, domain)
            worksheet.write(i, col+2, industry)
            worksheet.write(i, col+3, campaign_name)
            worksheet.write(i, col+4, internal_id)
            worksheet.write(i, col+5, external_id)
            worksheet.write(i, col+6, 'Y')

    workbook.close()

<<<<<<< HEAD
excel_writer('C:\\Users\\donnv\\Desktop\\test.xlsx', 'C:\\Users\\donnv\\Desktop\\20-1174-4 Whitelist.xlsx', '', 'TCI 20-1174-4', '2011744', '2011744')
=======
excel_writer('C:\\Users\\donnv\\Desktop\\test.xlsx', 'C:\\Users\\donnv\\Desktop\\output.xlsx', 'industry', 'campaign_name', 'internal_id', 'external_id')
>>>>>>> 78337c77dba0767c4168c30fd4f1e3e7585cd5b7
