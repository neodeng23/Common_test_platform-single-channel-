from test_station_2 import *
from Update_data import *
import sys
from logger import Logger
import globalvar as gl

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
        # 按键绑定信号
        self.Start_Button.clicked.connect(self.click_start)
        self.Start_Button.clicked.connect(self.label_time.timestart)
        # SN码输入绑定信号
        self.serial_number_line.returnPressed.connect(self.click_start)
        self.serial_number_line.returnPressed.connect(self.label_time.timestart)
        self.thread.sinOut.connect(self.test_Add)

    def click_start(self):
        # 获取SN
        serial_number = self.serial_number_line.text()

        # 初始化Log
        gl._init()
        now_time = time.strftime('%Y%m%d-%H%M%S')
        path = "E:\station_log\\" + serial_number + "\\" + now_time + "\\"
        WhetherPathExist(path)
        LOG_path = path + "test.log"
        log = Logger(LOG_path)
        gl.set_value('SN', serial_number)
        gl.set_value('path', path)
        gl.set_value('log_func', log)   # 将生成Log实例化对象设为全局变量

        # SN输入框无法编辑
        self.serial_number_line.setReadOnly(True)
        # 表格设置为空
        self.Test_Item.setRowCount(0)
        self.Test_Item.clearContents()
        # 开始按键变灰
        self.Start_Button.setEnabled(False)
        # 改变测试标签状态
        self.label_status.setText("Runing")
        self.label_status.setPalette(pe_yel)
        # 测试线程开始
        self.thread.start()

    def test_Add(self, test_item_res):
        # print(test_item_res)

        # 此条件为测试正在进行中
        if test_item_res[0] == "Running":
            self.Test_Item.update_item_data(test_item_res)

        # 此条件为测试结束
        elif test_item_res[0] == "Test_Fail!!!!" or test_item_res[0] == "All_Pass!!!!":
            self.Test_Item.update_item_data(test_item_res)
            self.label_time.timestop()
            self.Test_Item.handleSave()
            self.serial_number_line.setReadOnly(False)
        else:
            self.Test_Item.update_item_data_without_add_new_line(test_item_res)
        self.Test_Item.scrollToBottom()
        if test_item_res[0] == 'All_Pass!!!!':
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
