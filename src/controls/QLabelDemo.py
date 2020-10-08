import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QApplication, QWidget


class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=yellow>这是一个文本标签.</font>')
        label1.setAutoFillBackground(True)
        # 调色板
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)  # 设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用 Python GUI 程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片')
        label3.setPixmap(QPixmap('./images/python.jpg'))

        label4.setText("<a href='http://item.jd.com/12417265.html'>感谢关注</a>")

        label4.setOpenExternalLinks(True)  # 设置为True使用浏览器打开网页，False调用槽函数
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def linkHovered(self):
        print('当鼠标划过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
