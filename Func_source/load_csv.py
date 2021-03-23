# coding=utf-8
import os
import re
import csv
import time
from datetime import datetime

path = "C:/Users/jsyzdlf/Desktop/"
#path = "C:/Users/Administrator/Desktop/"
csv_name = "test.csv"
csvFile = open(path + csv_name, newline='')

header_lines = ["enabled", "Step", "TestGroup", "TestName", "PortDevice", "RetryTimes", "Cmd", "SendEndSympol", "TimeOut", "CheckValue", "LowLimit", "UpLimit", "unit"]


def Initialize_test_table(csvFile, row_list=None):
    """
        0     "enabled",
        1     "Step",
        2     "TestGroup",
        3     "TestName",
        4     "PortDevice",
        5     "RetryTimes",
        6     "Cmd",
        7     "SendEndSympol",
        8     "TimeOut",
        9     "CheckValue",
        10    "LowLimit",
        11    "UpLimit",
        12    "unit"
    """
    if row_list is None:
        row_list = []
    reader = csv.reader(csvFile)
    for row in reader:
        row_list.append(row)
    if row_list[0] != header_lines:
        row_list = [["error"]]
    print("finish Initialize_test_table")
    return row_list


def Test_Csv_item(row_list, line_num):
    single_test_list = row_list[line_num]
    res, value, duration = Go_Test(single_test_list)
    if res == "pass":
        res = Test_input_UI(single_test_list, "pass", value, duration)
    else:
        res = Test_input_UI(single_test_list, "fail", value, duration)
    return res


def Go_Test(single_test_list):
    start_time = datetime.now()
    value = "23"
    time.sleep(3)
    time_elapsed = datetime.now() - start_time
    dur = format(time_elapsed)[:-2]
    return "pass", value, dur


def Test_input_UI(single_test_list, res, value, duration):
    Step = single_test_list[1]
    TestGroup = single_test_list[2]
    TestName = single_test_list[3]
    CMD = single_test_list[6]
    LowLimit = single_test_list[10]
    #value = value
    UpLimit = single_test_list[11]
    Unit = single_test_list[12]
    #duration = duration
    data = [res, Step, TestGroup, TestName, CMD, LowLimit, value, UpLimit, Unit, duration]
    return data


if __name__ == "__main__":
    row_list = Initialize_test_table(csvFile)
    print(row_list[1])
    print(len(row_list))
