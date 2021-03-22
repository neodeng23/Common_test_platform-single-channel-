from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from test_station_1 import *
import sys


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)


    def showtime(self):
        datetime = QTime.currentTime()
        text = datetime.toString()
        self.label_time.setText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainForm()

    mainWindow.show()
    sys.exit(app.exec_())