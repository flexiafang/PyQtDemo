import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton, QHBoxLayout, QWidget


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')
        # 设置窗口的尺寸
        self.resize(400, 300)
        # self.center()

        # 退出按钮
        self.button = QPushButton('退出')
        # 设置控件提示消息
        self.button.setToolTip('这是一个按钮，<b>OK</b>？')
        # 将信号与槽关联
        self.button.clicked.connect(self.onClickButton)

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

        # 状态栏
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)

    def center(self):
        """
        窗口居中
        """
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)

    def onClickButton(self):
        """
        按钮点击事件的方法（自定义槽）
        """
        sender = self.sender()
        print(sender.text() + ' 被按下')
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/tiger.ico'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
