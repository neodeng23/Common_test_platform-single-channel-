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
        self.setColumnCount(9)  # 设置列数
        # self.setColumnWidth(0, 200)  # 设置列宽(第几列， 宽度)
        # self.setRowHeight(0, 100)  # 设置行高(第几行， 行高)

        column_name = [
            'Step',
            'TestGroup',
            'TestName',
            'Result',
            'CMD',
            'LowLimit',
            'Value',
            'UpLimit',
            'Unit',
            'duration'
        ]
        self.setHorizontalHeaderLabels(column_name)  # 设置列名称
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);font:11pt '宋体';color: black;};")
            #"QHeaderView::section{background-color:rgb(40,143,218);font:13pt '宋体';color: white;};")

    def update_item_data(self, data):
        """更新内容"""
        self.setItem(0, 0, QTableWidgetItem(data))
        self.setItem(0, 1, QTableWidgetItem(data))  # 设置表格内容(行， 列) 文字


def add_line(self):
    row = self.table.rowCount()
    self.table.setRowCount(row + 1)
    id = str(self.id)