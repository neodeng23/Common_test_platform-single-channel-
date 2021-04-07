# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time


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

        #self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setDefaultSectionSize(117)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);font:11pt '宋体';color: black;};")
            #"QHeaderView::section{background-color:rgb(40,143,218);font:13pt '宋体';color: white;};")

    def update_item_data(self, data):
        """
        更新内容
        data = [res, Step, TestGroup, TestName, CMD, LowLimit, value, UpLimit, Unit, duration]
        """
        num = self.rowCount()
        self.insertRow(num)
        for line_num in range(0, len(data)):
            self.setItem(num, line_num, QTableWidgetItem(data[line_num]))  # 设置表格内容(行， 列) 文字
        self.change_res_color(data[0], num)
        # if data[0] == "pass" or data[0] == "All_Pass!!!!":
        #     self.item(num, 0).setBackground(QBrush(QColor(0, 255, 0)))
        # elif data[0] == "Running":
        #     self.item(num, 0).setBackground(QBrush(QColor(255, 255, 0)))
        # else:
        #     self.item(num, 0).setBackground(QBrush(QColor(255, 0, 0))) #红色

    def change_res_color(self, res, num):
        if res == "pass" or res == "All_Pass!!!!":
            self.item(num, 0).setBackground(QBrush(QColor(0, 255, 0)))
        elif res == "Running":
            self.item(num, 0).setBackground(QBrush(QColor(255, 255, 0)))
        else:
            self.item(num, 0).setBackground(QBrush(QColor(255, 0, 0))) #红色

    def update_item_data_without_add_new_line(self, data):
        """
        更新内容
        data = [res, Step, TestGroup, TestName, CMD, LowLimit, value, UpLimit, Unit, duration]
        """
        num = self.rowCount()
        for line_num in range(0, len(data)):
            self.setItem(num-1, line_num, QTableWidgetItem(data[line_num]))  # 设置表格内容(行， 列) 文字
        self.change_res_color(data[0], num-1)