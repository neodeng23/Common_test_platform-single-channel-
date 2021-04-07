from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from test_station_1 import *
from load_csv import *
from Update_data import *
import sys

pe_red = QPalette()
pe_red.setColor(QPalette.WindowText, Qt.red)

pe_green = QPalette()
pe_green.setColor(QPalette.WindowText, Qt.green)

pe_yel = QPalette()
pe_yel.setColor(QPalette.WindowText, Qt.yellow)


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.thread = Update_data()
        self.Start_Button.clicked.connect(self.click_start)
        self.thread.sinOut.connect(self.test_Add)

    def click_start(self):
        self.Test_Item.setRowCount(0)
        self.Test_Item.clearContents()
        self.Start_Button.setEnabled(False)
        self.label_status.setText("Runing")
        self.label_status.setPalette(pe_yel)
        self.thread.start()

    def test_Add(self, test_item_res):
        print(test_item_res)
        if test_item_res[0] == "Running":
            self.Test_Item.update_item_data(test_item_res)
        elif test_item_res[0] == "pass":
            num = self.Test_Item.rowCount()
            self.Test_Item.setItem(num-1, 0, QTableWidgetItem(test_item_res[0]))  # 设置表格内容(行， 列) 文字
            self.Test_Item.item(num-1, 0).setBackground(QBrush(QColor(0, 255, 0)))
        elif test_item_res[0] == "Test_Fail!!!!" or test_item_res[0] == "All_Pass!!!!":
            self.Test_Item.update_item_data(test_item_res)
        else:
            num = self.Test_Item.rowCount()
            self.Test_Item.setItem(num - 1, 0, QTableWidgetItem(test_item_res[0]))  # 设置表格内容(行， 列) 文字
            self.Test_Item.item(num - 1, 0).setBackground(QBrush(QColor(255, 0, 0)))
        self.Test_Item.scrollToBottom()
        if test_item_res[0] == 'All_Pass!!!!' :
            self.Start_Button.setEnabled(True)
            self.label_status.setText("Pass")
            self.label_status.setPalette(pe_green)
        elif test_item_res[0] == 'Test_Fail!!!!':
            self.Start_Button.setEnabled(True)
            self.label_status.setText("Fail")
            self.label_status.setPalette(pe_red)
        else:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainForm()
    mainWindow.show()
    sys.exit(app.exec_())
