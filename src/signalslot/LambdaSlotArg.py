import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QHBoxLayout, QMainWindow


class LambdaSlotArg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("使用Lambda表达式为槽函数传递参数")

        button1 = QPushButton("按钮1")
        button2 = QPushButton("按钮2")
        ok = 100
        button1.clicked.connect(lambda: self.onButtonClick(10, ok))
        button2.clicked.connect(lambda: self.onButtonClick(ok, -20))
        button1.clicked.connect(lambda: QMessageBox.information(self, "结果", "单击了button1"))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onButtonClick(self, m, n):
        print("m + n =", m + n)
        QMessageBox.information(self, "结果", str(m + n))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = LambdaSlotArg()
    form.show()
    sys.exit(app.exec_())
