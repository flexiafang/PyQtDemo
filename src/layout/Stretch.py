import sys

from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QApplication, QWidget


class Stretch(QWidget):
    def __init__(self):
        super(Stretch, self).__init__()
        self.setWindowTitle("设置伸缩量")
        self.resize(800, 200)

        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn4 = QPushButton(self)
        btn5 = QPushButton(self)
        btn1.setText("按钮1")
        btn2.setText("按钮2")
        btn3.setText("按钮3")
        btn4.setText("按钮4")
        btn5.setText("按钮5")

        layout = QHBoxLayout()

        layout.addStretch(0)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        layout.addStretch(1)
        layout.addWidget(btn4)
        layout.addWidget(btn5)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Stretch()
    main.show()
    sys.exit(app.exec_())
