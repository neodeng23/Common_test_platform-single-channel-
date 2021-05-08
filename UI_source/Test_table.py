# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import globalvar as gl
import csv
import os
from function import WhetherPathExist, get_test_name_list, handle_summary_log

header_lines = ["res", "Step", "TestGroup", "TestName", "CMD", "LowLimit", "value", "UpLimit", "Unit", "duration"]


def add_log_summary(data):
    """
    判断summary log是否存在，若存在将追加，不存在将会创建
    """
    now_day = gl.get_value('now_day')
    summary_path = gl.get_value('summary_path')
    WhetherPathExist(summary_path)
    summary_csv_name = summary_path + now_day + ".csv"
    flag = os.path.isfile(summary_csv_name)
    if flag:
        with open(summary_csv_name, 'a', newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(data)
            pass
    else:
        test_name_list = get_test_name_list()
        test_name_list.insert(0, "SN")
        test_name_list.append("duration")
        with open(summary_csv_name, 'w', newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(test_name_list)
            writer.writerow(data)


class MyTable(QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("Test_Item")  # 设置表格名称
        self.resize(600, 200)  # 设置表格尺寸（整体大小）
        self.setColumnCount(10)  # 设置列数
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.scrollToBottom()
        # self.setColumnWidth(0, 200)  # 设置列宽(第几列， 宽度)
        # self.setRowHeight(0, 100)  # 设置行高(第几行， 行高)

        column_name = [
            'Result',
            'Step',
            'TestGroup',
            'TestName',
            'CMD',
            'LowLimit',
            'Value',
            'UpLimit',
            'Unit',
            'duration'
        ]
        self.setHorizontalHeaderLabels(column_name)  # 设置列名称

        # self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setDefaultSectionSize(117)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);font:11pt '宋体';color: black;};")
        # "QHeaderView::section{background-color:rgb(40,143,218);font:13pt '宋体';color: white;};")

    def update_item_data(self, data):
        """
        实时向UI界面表格中更新数据，新增一行
        更新内容 data = [res, Step, TestGroup, TestName, CMD, LowLimit, value, UpLimit, Unit, duration]
        """
        num = self.rowCount()
        self.insertRow(num)
        for line_num in range(0, len(data)):
            self.setItem(num, line_num, QTableWidgetItem(data[line_num]))  # 设置表格内容(行， 列) 文字
        self.change_res_color(data[0], num)

    def change_res_color(self, res, num):
        if res == "pass" or res == "All_Pass!!!!":
            self.item(num, 0).setBackground(QBrush(QColor(0, 255, 0)))
        elif res == "Running":
            self.item(num, 0).setBackground(QBrush(QColor(255, 255, 0)))
        else:
            self.item(num, 0).setBackground(QBrush(QColor(255, 0, 0)))  # 红色

    def update_item_data_without_add_new_line(self, data):
        """
        实时像UI界面表格中更新数据，更新在当前的最后一行，不新增行
        更新内容 data = [res, Step, TestGroup, TestName, CMD, LowLimit, value, UpLimit, Unit, duration]
        """
        num = self.rowCount()
        for line_num in range(0, len(data)):
            self.setItem(num - 1, line_num, QTableWidgetItem(data[line_num]))  # 设置表格内容(行， 列) 文字
        self.change_res_color(data[0], num - 1)

    def handleSave(self):
        log = gl.get_value('log_func')
        SN = gl.get_value('SN')
        log_path = gl.get_value('path')  # "D:\station_log\\" + serial_number + "\\"
        csv_name = log_path + SN + ".csv"
        log.logger.info("开始记录全部测试结果，路径为： " + log_path)
        All_update_data = []
        # 写入csv log
        with open(csv_name, 'w', newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(header_lines)
            for row in range(self.rowCount()):
                rowdata = []
                for column in range(self.columnCount()):
                    item = self.item(row, column)
                    if item is not None:
                        rowdata.append(
                            item.text())
                    else:
                        rowdata.append('')
                log.logger.info(rowdata)
                All_update_data.append(rowdata)
                writer.writerow(rowdata)
        up_to_sum_data = handle_summary_log(All_update_data, SN)
        # 写入summary csv log
        print(up_to_sum_data)
        add_log_summary(up_to_sum_data)
