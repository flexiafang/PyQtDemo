import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class WindowPattern(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)
        self.setWindowTitle('设置窗口的样式')

        self.setWindowFlags(
            # Qt.WindowMaximizeButtonHint |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowStaysOnTopHint |
            Qt.WindowCloseButtonHint)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(images/python.jpg);}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowPattern()
    window.show()
    sys.exit(app.exec_())
