# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from run import *
from load_csv import *
import sys
import time


#path = "C:/Users/jsyzdlf/Desktop/"
path = "C:/Users/Administrator/Desktop/"
csv_name = "test.csv"


class Update_data(QThread):
    """更新数据类"""
    sinOut = pyqtSignal(list)

    def __init__(self, parent=None):
        super(Update_data, self).__init__(parent)
        #设置工作状态与初始num数值
        self.working = True

    def run(self):
        csvFile = open(path + csv_name, newline='')
        row_list = Initialize_test_table(csvFile)
        line_num = len(row_list)
        for test_item in range(1, line_num):
            updata_data = Test_Csv_item(row_list, test_item)
            print(updata_data)
            self.sinOut.emit(updata_data)
            time.sleep(0.5)
