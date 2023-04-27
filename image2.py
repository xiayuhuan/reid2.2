import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from PyQt5.QtGui import QIcon
import os
import time

a = ['1位置：摄像头c1小区A, 时间：10:11:19','2位置：摄像头c3小区C, 时间：10:43:44',
'3位置：摄像头c3小区C, 时间：10:43:52','4位置：摄像头c3小区C, 时间：10:50:27',
'5位置：摄像头c1小区A, 时间：10:11:21','6位置：摄像头c1小区A, 时间：10:11:24',
'7位置：摄像头c1小区A, 时间：10:18:05','8位置：摄像头c3小区C, 时间：10:50:23',
'9位置：摄像头c6小区F, 时间：10:01:19','10位置：摄像头c6小区F, 时间：10:59:39']

class Qt_Window(QWidget):
    my_signal = pyqtSignal(str)

    def __init__(self):
        self._app = QtWidgets.QApplication([])
        super(Qt_Window, self).__init__()
        self.msg_history = list()  # 用来存放消息

    def init_ui(self):
        self.win = QMainWindow()
        self.win.setWindowTitle("行人重识别系统")
        self.win.setWindowIcon(QIcon('people1.png'))

        # self.comboBox = QComboBox(self.win)
        self.comboBox = QComboBox(self.win)#图片选择框
        self.number_lable = QLabel(self.win)
        self.close_Button = QPushButton(self.win)
        self.detect_image = QLabel(self.win)
        self.msg = QLabel(self.win)#行人追踪结果
        # self.msg1 = QLabel("")  # 显示行人信息

        self.msg1 = QLabel(self.win)  # 显示行人信息


        # 设置路径
        self.path = ("D:/shijian/bishe/PYQT/PYQT/qtceshi/query")

        self.comboBox.resize(100, 25)
        self.comboBox.move(100, 400)#图片
        # self.comboBox.setGeometry(20, 20, 30, 20)
        self.img_list = os.listdir(self.path)
        self.comboBox.addItems([self.img_list[i] for i in range(len(self.img_list))])
        self.comboBox.activated.connect(self.show_img)

        self.close_Button.resize(100, 25)#退出
        self.close_Button.move(300, 400)
        # self.open_Button.setGeometry(50, 80, 70, 30)
        self.close_Button.setText("退出")
        self.close_Button.clicked.connect(self.exit)
        # self.close_Button.mouseDoubleClickEvent.connect(self.exit)

        self.detect_image.resize(100, 200)#图片显示
        self.detect_image.move(100, 150)#图片显示位置

        self.msg.resize(440, 15)
        self.msg.move(300,100)
        self.msg.setText("行人追踪结果")

        self.msg1.resize(440, 17)
        # self.msg1.setStyleSheet("QLabel{border:2px solid rgb(0, 255, 0);}");
        self.msg1.move(300, 120)
        # self.msg1.setText("行人追踪结果1")
        self.msg1.setWordWrap(True)  # 自动换行

        # 创建一个滚动对象
        self.scroll = QScrollArea(self.win)
        self.scroll.move(300,120)
        self.scroll.resize(380,300)
        self.scroll.setWidget(self.msg1)
        # self.scroll.setStyleSheet("QLabel{border:2px solid rgb(0, 255, 0);}")

        # self.comboBox.Click.connect(self.check)
        # self.comboBox.mouseDoubleClickEvent(self.check)
        self.comboBox.currentIndexChanged.connect(
            lambda: self.model_init(self.comboBox.currentIndex()))

        # model_init函数的实现的核心代码
        # 加载相关参数，并初始化模型

        print("hello")


        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)


        # self.number_lable.resize(100, 25)
        # self.number_lable.move(450, 350)
        self.win.resize(700, 500)

        self.win.show()
        sys.exit(self._app.exec_())

    def model_init(self, tag):
        if tag is not None:
            print("tag:",tag)
            for i, ip in enumerate(a):
                msg1 = ip
                # print(msg)
                # if i % 5 == 3:
                # 表示发射信号 对象.信号.发射(参数)
                self.my_signal.emit(msg1)
                time.sleep(0.01)
            # self.check

        # if tag == 1:  # 当下拉框选中"1"触发事件
        #     """
        #     代码省略
        #     """


    def show_img(self):
        img = self.comboBox.currentText()
        pix = QPixmap(self.path + "\\" + img)
        self.detect_image.setPixmap(pix)
        self.detect_image.setScaledContents(True)
        lable = img.split(".")[0]
        # self.number_lable.setText(lable)

    def my_slot(self, msg1):
        # 更新内容
        print("msg1:",msg1)
        self.msg_history.append(msg1)
        self.msg1.setText("<br>".join(self.msg_history))
        self.msg1.resize(440, self.msg1.frameSize().height() + 17)
        self.msg1.repaint()  # 更新内容，如果不更新可能没有显示新内容

    def check(self):
        for i, ip in enumerate(a):
            msg1 = ip
            # print(msg)
            # if i % 5 == 3:
                # 表示发射信号 对象.信号.发射(参数)
            self.my_signal.emit(msg1)
            time.sleep(0.01)


    def exit(self):
        while True:
            sys.exit(0)

if __name__ == '__main__':
    s = Qt_Window()
    s.init_ui()