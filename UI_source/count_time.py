from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QApplication, QLCDNumber
from PyQt5.QtCore import QTime, QTimer
import sys


class ShowTime(QWidget):
    def __init__(self, parent=None):
        super(ShowTime, self).__init__(parent)
        self.isTimeStart = False  # 标记时间是否开始计时
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(8)
        self.lcd.setStyleSheet("border: 1px solid black; color: black; background: silver;")
        self.lcd.display("00:00:00")
        # self.lable_time = QLabel('运行时间：', self)
        # self.lable_time_val = QLabel('00:00:00', self)
        self.btn_start = QPushButton('开始显示')
        self.btn_stop = QPushButton('停止计时')
        # 创建定时器对象和时间对象
        self.timer = QTimer()  #
        self.timeClock = QTime()

        # 信号与槽
        # self.btn_start.clicked.connect(self.timestart)
        self.timer.timeout.connect(self.addtime)
        # self.btn_stop.clicked.connect(self.timestop)

    def back_to_zero(self):
        self.lcd.setDigitCount(8)
        self.lcd.display("00:00:00")

    def timestart(self):  # 启动计时
        if not self.isTimeStart:
            self.timeClock.setHMS(0, 0, 0)  # 初始时设置时间为  00：00：00
            self.timer.start(1000)  # 启动定时器，定时器对象每隔一秒发射一个timeout信号
        self.isTimeStart = True

    def addtime(self):  # 计时时间增一秒，并显示在QLable上
        self.timeClock = self.timeClock.addMSecs(1000)  # 时间增加一秒
        #self.lable_time_val.setText(self.timeClock.toString("hh:mm:ss"))  # 标签显示时间
        print(self.timeClock.toString("hh:mm:ss"))
        self.lcd.display(self.timeClock.toString("hh:mm:ss"))  # 标签显示时间

    def timestop(self):  # 停止计时
        if self.isTimeStart:
            self.timer.stop()
            self.isTimeStart = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ShowTime()
    demo.show()
    sys.exit(app.exec())