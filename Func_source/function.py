# coding=utf-8
import os
import re
import csv
import time
from serial_test import serial_send_cmd
from datetime import datetime
import globalvar as gl


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
    log = gl.get_value('log_func')
    if row_list is None:
        row_list = []
    reader = csv.reader(csvFile)
    for row in reader:
        row_list.append(row)
    if row_list[0] != header_lines:
        row_list = [["error"]]
    log.logger.info("finish Initialize_test_table")
    return row_list


def Test_Csv_item(row_list, line_num):
    single_test_list = row_list[line_num]
    res, value, duration = Go_Test(single_test_list)
    if res == "pass":
        res = Test_input_UI(single_test_list, "pass", value, duration)
    else:
        res = Test_input_UI(single_test_list, "fail", value, duration)
    return res


def Get_Csv_item(row_list, line_num):
    single_test_list = row_list[line_num]
    res = Test_input_UI(single_test_list, "Running", '', '')
    return res


def Go_Test(single_test_list):
    """
    :param single_test_list: test.csv中的一行
    :return: 测试结果，测试值，测试时间
    """
    log = gl.get_value('log_func')
    res = "pass"
    value = "23"
    start_time = datetime.now()
    test_step = single_test_list[1]
    test_device = single_test_list[4]
    SendEndSympol = single_test_list[7]
    test_cmd = single_test_list[6]
    TimeOut = single_test_list[8]
    if test_step == "UartCom":
        try:
            value = serial_send_cmd(test_device, test_cmd, TimeOut, SendEndSympol)
        except:
            value = "fail send cmd"
    elif test_step == "script":
        pass
    elif test_step == "CutOut":
        pass
    elif test_step == "Judge":
        pass
    elif test_step == "VisaCom":
        pass
    elif test_step == "FeasaCom":
        pass
    else:
        res = "Error"
        value = "Error step"
    time.sleep(0.5)
    # 待添加limits功能
    time_elapsed = datetime.now() - start_time
    dur = format(time_elapsed)[:-2]
    log.logger.info("\n" +
                    "test_device: " + test_device + ";\n" +
                    "test_cmd: " + test_cmd + ";\n" +
                    "test_res: " + res + ";\n" +
                    "test_value: " + value + ".")
    return res, value, dur


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


def WhetherPathExist(path):
    """
    :param 路径
    :return: 检查路径是否存在，若不存在则创建此路径
    """
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)


def Check_value(value):
    pass


if __name__ == "__main__":
    pass
