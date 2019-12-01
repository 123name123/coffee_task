from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QPolygon
import sys
from random import randrange


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setMouseTracking(True)
        self.pushButton.clicked.connect(self.changepos)
        self.flag = 0

    def changepos(self):
        self.flag += 1
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for i in range(self.flag):
            self.paint(qp)
        qp.end()

    def paint(self, qp):
        if self.flag:
            qp.setBrush(QColor(255, 255, 0))
            ch = randrange(100)
            qp.drawEllipse(randrange(400), randrange(400), ch, ch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
