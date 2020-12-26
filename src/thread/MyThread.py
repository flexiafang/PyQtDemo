from PyQt5.QtCore import QThread, pyqtSignal


class MyThread(QThread):
    displaySignal = pyqtSignal(str)

    def __init__(self, number=0, parent=None):
        super(MyThread, self).__init__(parent)
        self.number = number
        self.keepRunning = True

    def stop(self):
        self.keepRunning = False

    def run(self):
        id = int(self.currentThreadId())
        i = 0
        while self.keepRunning:
            i += 1
            self.displaySignal.emit('Thread {:>2} ==> ( ID={:>5}, val={:>3} )'.format(self.number, id, i))
            self.msleep(1000)
        self.keepRunning = True
