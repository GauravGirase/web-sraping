import time
import xlsxwriter


def populate_data_in_csv_file(data):
    workbook = xlsxwriter.Workbook("users.xlsx")
    worksheet = workbook.add_worksheet("users")

    worksheet.write('A1', 'NAME')
    worksheet.write('B1', 'EMAIL')
    worksheet.write('C1', 'LOCALE')
    worksheet.write('D1', 'ROLES')

    row_index = 2
    for user_detail in data:
        worksheet.write('A' + str(row_index), user_detail['name'])
        worksheet.write('B' + str(row_index), user_detail['email'] )
        worksheet.write('C' + str(row_index), user_detail['locale'])
        worksheet.write('D' + str(row_index), user_detail['roles'])

        row_index += 1

    workbook.close()


def loading(msg1, msg2):
    print(msg1)
    time.sleep(5)
    print(msg2)
