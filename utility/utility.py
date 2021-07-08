import csv
import time

def populate_data_in_csv_file(data):
    rows = []
    for user_detail in data:
        rows.append(list(user_detail.values()))
    fields = ['Name', 'email', 'locale', 'roles']
    with open("users_records.csv", 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

def loading(msg1, msg2):
    print(msg1)
    time.sleep(5)
    print(msg2)
