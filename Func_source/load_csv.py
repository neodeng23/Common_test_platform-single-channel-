# coding=utf-8
import os
import re
import csv

# path = "C:/Users/jsyzdlf/Desktop/"
path = "C:/Users/Administrator/Desktop/"
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
        row_list = ["error"]
    return row_list
