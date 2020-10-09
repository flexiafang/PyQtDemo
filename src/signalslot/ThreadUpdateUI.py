import sys
import time

from PyQt5.QtCore import QDateTime, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QDialog, QLabel


class BackendThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(currentTime)
            time.sleep(1)


class ThreadUpdateUI(QDialog):
    def __init__(self):
        super(ThreadUpdateUI, self).__init__()
        self.setWindowTitle('多线程更新UI数据')
        self.resize(400, 100)
        self.input = QLabel(self)
        self.input.resize(400, 100)

        self.initUI()

    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)

        self.backend.start()

    def handleDisplay(self, data):
        self.input.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = ThreadUpdateUI()
    example.show()
    sys.exit(app.exec_())
