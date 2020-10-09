import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget


class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot, self).__init__()
        self.okButton = QPushButton("ok", self)
        self.okButton.setObjectName("okButton")

        self.cancelButton = QPushButton("cancel", self)
        self.cancelButton.setObjectName("cancelButton")

        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        layout.addWidget(self.cancelButton)
        self.setLayout(layout)

        # self.okButton.clicked.connect(self.on_okButton_clicked)
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print("点击了ok按钮")

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print("点击了cancel按钮")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = AutoSignalSlot()
    example.show()
    sys.exit(app.exec_())
