import time
import os
import csv
from function import *

header_lines = ["enabled", "Step", "TestGroup", "TestName", "PortDevice", "RetryTimes", "Cmd", "SendEndSympol", "TimeOut", "CheckValue", "LowLimit", "UpLimit", "unit"]


test_name_list = []
csvFile = open("E:\\test_config\\test.csv", newline='')
row_list = Initialize_test_table(csvFile)
for i in range(1, len(row_list)):
    a = row_list[i][3]
    test_name_list.append(a)

test_name_list.insert(0, "SN")
test_name_list.append("duration")
print(test_name_list)

now_day = time.strftime('%Y%m%d')
summary_csv_name = "E:\\station_log\\summary_log\\" + now_day + ".csv"
flag = os.path.isfile(summary_csv_name)
if flag:
    with open(summary_csv_name, 'a', newline="") as stream:
        writer = csv.writer(stream)
        pass
else:
    test_name_list = get_test_name_list()
    test_name_list.insert(0, "SN")
    test_name_list.append("duration")
    with open(summary_csv_name, 'w', newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(test_name_list)
pass


