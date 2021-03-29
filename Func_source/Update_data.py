# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from load_csv import *
import sys
import time

# path = "C:/Users/jsyzdlf/Desktop/"
# path = "C:/Users/Administrator/Desktop/"
path = "C:/test_config/"

csv_name = "test.csv"


class Update_data(QThread):
    """更新数据类"""
    sinOut = pyqtSignal(list)

    def __init__(self, parent=None):
        super(Update_data, self).__init__(parent)
        # 设置工作状态与初始num数值
        self.working = True
        self.flag = 1

    def run(self):
        test_start_time = datetime.now()
        res_flag = 0
        try:
            csvFile = open(path + csv_name, newline='')
            row_list = Initialize_test_table(csvFile)
        except:
            res_flag = 1
            row_list = [["invaild csv"]]
        line_num = len(row_list)
        for test_item in range(1, line_num):
            updata_data = Test_Csv_item(row_list, test_item)
            self.sinOut.emit(updata_data)
            if updata_data[0] != "pass":
                res_flag = 1
            else:
                pass
        test_time_elapsed = datetime.now() - test_start_time
        total_time = format(test_time_elapsed)[:-2]
        if res_flag == 0:
            res_pass = ['All_Pass!!!!', '', '', '', '', '', '', '', '', total_time]
            self.sinOut.emit(res_pass)
        else:
            res_fail = ['Test_Fail!!!!', '', '', '', '', '', '', '', '', total_time]
            self.sinOut.emit(res_fail)
