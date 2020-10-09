import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class OverrideSlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Override（覆盖）槽函数")

    '''
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Alt:
            self.setWindowTitle("按下Alt键")
    '''

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == Qt.Key_Escape:
            self.close()
        elif a0.key() == Qt.Key_Alt:
            self.setWindowTitle("按下Alt键")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = OverrideSlot()
    form.show()
    sys.exit(app.exec_())
