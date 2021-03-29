from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from test_station_1 import *
from load_csv import *
from Update_data import *
import sys


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.thread = Update_data()
        self.Start_Button.clicked.connect(self.click_start)
        self.thread.sinOut.connect(self.test_Add)

    def click_start(self):
        self.Start_Button.setEnabled(False)
        self.thread.start()

    def test_Add(self, test_item_res):
        self.Test_Item.update_item_data(test_item_res)
        self.Test_Item.scrollToBottom()
        if test_item_res[0] == 'All_Pass!!!!' or 'Test_Fail!!!!':
            self.Start_Button.setEnabled(True)
        else:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainForm()
    mainWindow.show()
    sys.exit(app.exec_())
