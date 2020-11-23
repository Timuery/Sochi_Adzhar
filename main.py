from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QPainter, QPen, QColor, QPolygon
from PyQt5.QtCore import Qt, QPoint, QPointF
import random
import math
import UI

class MyDrawWidget(QWidget):

    def __init__(self):
        super(MyDrawWidget, self).__init__()

        self.myFlag = -1

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        for i in range(30):
            self.drawOval(qp, i)
        qp.end()

    def drawOval(self, qp, i):

        if self.myFlag == -1:
            return

        elif self.myFlag == 0:
            r, g, b, a = 255, 255, 0, 255
            qp.setBrush(QColor(r, g, b, a))
            x, y = random.randint(1, self.width() - 2), random.randint(1, self.height() - 2)
            if x < self.width() // 2:
                w = random.randint(1, 100)
            else:
                w = random.randint(1, 100)
            if y < self.height() // 2:
                h = w
            else:
                h = w
            qp.drawEllipse(QPoint(x, y), w, h)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    deskX, deskY = QApplication.desktop().width(), QApplication.desktop().height()

    window = UI.MainWindow("Лабораторная 4", deskX // 2 - 500, deskY // 2 - 400, 1000, 800)
    window.show()
    sys.exit(app.exec())