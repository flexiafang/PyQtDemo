import sys

from PyQt5.QtWidgets import QWidget, QTextEdit, QFrame, QHBoxLayout, QPushButton, QVBoxLayout, QApplication

from src.thread.MyThread import MyThread


class MyWnd(QWidget):
    def __init__(self):
        super(MyWnd, self).__init__()

        self.txtEdit = QTextEdit()
        self.txtEdit.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        btnLayout = QHBoxLayout()
        btnNames = ["创建新线程", "停止所有线程", "退出程序"]
        slotFuncs = [self.slotCreateNewThread, self.slotStopAllThread, self.close]

        for btnName, slotFunc in zip(btnNames, slotFuncs):
            btn = QPushButton(btnName)
            btn.setMinimumSize(120, 40)
            btnLayout.addWidget(btn)
            btn.clicked.connect(slotFunc)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.txtEdit)
        mainLayout.addLayout(btnLayout)

        # 使用列表存储所有创建的线程
        self.allThreads = []
        self.setWindowTitle("多线程入门案例")
        self.resize(400, 300)

    def slotCreateNewThread(self):
        thread = MyThread(len(self.allThreads))
        thread.displaySignal.connect(self.slotDisplay)
        thread.start()
        self.allThreads.append(thread)

    def slotStopAllThread(self):
        for thread in self.allThreads:
            if thread.isRunning():
                thread.stop()
        del self.allThreads[:]

    def slotDisplay(self, val):
        self.txtEdit.append(val)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MyWnd()
    wnd.show()
    sys.exit(app.exec_())
