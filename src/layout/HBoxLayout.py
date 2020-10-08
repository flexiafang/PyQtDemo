import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class HBoxLayout(QWidget):
    def __init__(self):
        super(HBoxLayout, self).__init__()
        self.setWindowTitle('水平盒布局')
        self.resize(500,300)

        hLayout = QHBoxLayout()
        hLayout.addWidget(QPushButton('按钮1'), 1, Qt.AlignLeft | Qt.AlignTop)
        hLayout.addWidget(QPushButton('按钮2'), 2, Qt.AlignLeft | Qt.AlignTop)
        hLayout.addWidget(QPushButton('按钮3'), 1, Qt.AlignLeft | Qt.AlignTop)
        hLayout.addWidget(QPushButton('按钮4'), 1, Qt.AlignLeft | Qt.AlignBottom)
        hLayout.addWidget(QPushButton('按钮5'), 1, Qt.AlignLeft | Qt.AlignBottom)

        hLayout.setSpacing(40)
        self.setLayout(hLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HBoxLayout()
    main.show()
    sys.exit(app.exec_())
