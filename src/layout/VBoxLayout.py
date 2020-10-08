import sys

from PyQt5.QtWidgets import *


class VBoxLayout(QWidget):
    def __init__(self):
        super(VBoxLayout, self).__init__()
        self.setWindowTitle('垂直盒布局')
        self.resize(500, 300)

        vLayout = QVBoxLayout()
        vLayout.addWidget(QPushButton('按钮1'))
        vLayout.addWidget(QPushButton('按钮2'))
        vLayout.addWidget(QPushButton('按钮3'))
        vLayout.addWidget(QPushButton('按钮4'))
        vLayout.addWidget(QPushButton('按钮5'))

        vLayout.setSpacing(40)
        self.setLayout(vLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VBoxLayout()
    main.show()
    sys.exit(app.exec_())
