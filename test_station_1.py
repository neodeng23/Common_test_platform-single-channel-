# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_station_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Test_table import MyTable


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1194, 793)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 451, 121))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 30, 91, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 80, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 130, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 190, 451, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 190, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.Attributes = QtWidgets.QTableView(self.centralwidget)
        self.Attributes.setGeometry(QtCore.QRect(660, 130, 521, 101))
        self.Attributes.setObjectName("Attributes")

        self.Test_Item = MyTable(self.centralwidget)
        self.Test_Item.setGeometry(QtCore.QRect(10, 250, 1171, 491))
        self.Test_Item.setObjectName("Test_Item")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(980, 20, 191, 71))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 10, 51, 31))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(660, 50, 51, 31))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(660, 90, 51, 31))
        self.label_5.setObjectName("label_5")

        self.pass_num = QtWidgets.QTableView(self.centralwidget)
        self.pass_num.setGeometry(QtCore.QRect(720, 20, 161, 21))
        self.pass_num.setObjectName("Attributes_2")

        self.fail_num = QtWidgets.QTableView(self.centralwidget)
        self.fail_num.setGeometry(QtCore.QRect(720, 60, 161, 21))
        self.fail_num.setObjectName("Attributes_3")

        self.total_num = QtWidgets.QTableView(self.centralwidget)
        self.total_num.setGeometry(QtCore.QRect(720, 90, 161, 21))
        self.total_num.setObjectName("Attributes_4")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1194, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Normal_Test"))
        self.pushButton.setText(_translate("MainWindow", "Normal_Test"))
        self.pushButton_2.setText(_translate("MainWindow", "Offline_Test"))
        self.pushButton_3.setText(_translate("MainWindow", "Loop_Test"))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "time"))
        self.label_3.setText(_translate("MainWindow", "Pass"))
        self.label_4.setText(_translate("MainWindow", "Fail"))
        self.label_5.setText(_translate("MainWindow", "Total"))
