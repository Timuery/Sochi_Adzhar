from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QPainter, QPen, QColor, QPolygon
from PyQt5.QtCore import Qt, QPoint, QPointF
import random
import math
import main

class MainWindow(QWidget):

    def __init__(self, title, x, y, width, height):
        super(MainWindow, self).__init__()

        self.setGeometry(x, y, width, height)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon("1.jpeg"))

        self.initGUI()

    def initGUI(self):
        # upperLay

        uWidget = main.MyDrawWidget()

        # lowerLay

        names = ["Круги"]
        self.btns = []

        lLay = QHBoxLayout()
        for i, name in enumerate(names):
            btn = QPushButton(name)
            btn.clicked.connect(lambda ch, i=i: self.btnClicked(uWidget, i))
            lLay.addWidget(btn)
            self.btns.append(btn)

        lWidget = QWidget()
        lWidget.setLayout(lLay)

        mLay = QVBoxLayout()
        mLay.addWidget(uWidget, 9)
        mLay.addWidget(lWidget, 1)

        self.setLayout(mLay)

    def btnClicked(self, uWidget, i):
        uWidget.myFlag = i
        self.update()

