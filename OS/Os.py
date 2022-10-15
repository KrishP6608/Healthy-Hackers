from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy
import sys
import time
import os
def minute_passed(oldepoch):
    return time.time() - oldepoch >= 300

class Okno(QMainWindow):
    def __init__(self):
        super(Okno, self).__init__()
        self.setStyleSheet("background-image : url(bg (2).png)")
        self.setGeometry(500, 500, 900, 500)
        self.setWindowTitle("My window")
        self.label = QtWidgets.QLabel()
        self.calculator = QtWidgets.QPushButton()
        self.calculator.setGeometry(100, 100, 1200, 200)
        self.exit = QtWidgets.QPushButton()
        self.health = QtWidgets.QPushButton()
        self.notepad = QtWidgets.QPushButton()
        self.browser = QtWidgets.QPushButton()
        self.terminal = QtWidgets.QPushButton()
        self.water = QtWidgets.QPushButton()
        self.iniUI()

    # Buttons
    def iniUI(self):
        w = QtWidgets.QWidget()
        self.setCentralWidget(w)
        grid = QtWidgets.QGridLayout(w)

        self.calculator.setText("calculator")
        self.calculator.move(200, 200)
        self.calculator.setMinimumWidth(150)
        self.calculator.clicked.connect(self.calcu)


        self.water.setText("Water")
        self.water.clicked.connect(self.wat)

        self.browser.setText("Browser")
        self.browser.clicked.connect(self.bro)

        self.notepad.setText("Note")
        self.notepad.clicked.connect(self.note)

        self.terminal.setText("Terminal")
        self.terminal.clicked.connect(self.ter)

        self.exit.setText("Exit")
        self.exit.clicked.connect(self.close)


        grid.addWidget(self.calculator, 0, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
        grid.addWidget(self.exit, 0, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        grid.addWidget(self.water, 0, 2, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        grid.addWidget(self.health, 0, 3, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        grid.addWidget(self.notepad, 0, 4, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        grid.addWidget(self.browser, 0, 5, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        grid.addWidget(self.terminal, 0, 6, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)

        self.water.move(200, 100)


    def calcu(self):
        os.system('python Calculator.py')

    def wat(self):
        os.system('python water.py')

    def note(self):
        os.system('python NotePad.py')

    def heal(self):
        os.system('python health.py')

    def ter(self):
        os.system('python terminal.py')

    def bro(self):
        os.system('python browser.py')


def window():
    start = time.time()
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec_())

window()