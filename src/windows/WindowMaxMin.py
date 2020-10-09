import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget


class WindowMaxMin(QWidget):
    def __init__(self, parent=None):
        # 调用父类构造函数
        super(WindowMaxMin, self).__init__(parent)
        self.resize(300, 400)
        self.setWindowTitle("用代码控制窗口的最大化和最小化")
        self.setWindowFlags(Qt.WindowMaximizeButtonHint)

        layout = QVBoxLayout()

        maxButton1 = QPushButton(self)
        maxButton1.setText('窗口最大化1')
        maxButton1.clicked.connect(self.maximized)

        maxButton2 = QPushButton(self)
        maxButton2.setText('窗口最大化2')
        maxButton2.clicked.connect(self.showMaximized)

        minButton = QPushButton()
        minButton.setText('窗口最小化')
        minButton.clicked.connect(self.showMinimized)

        layout.addWidget(maxButton1)
        layout.addWidget(maxButton2)
        layout.addWidget(minButton)
        self.setLayout(layout)

    def maximized(self):
        # 获取桌面可用尺寸
        desktop = QApplication.desktop()
        rect = desktop.availableGeometry()
        self.setGeometry(rect)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowMaxMin()
    window.show()
    sys.exit(app.exec_())
