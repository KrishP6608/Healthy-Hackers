import PyQt5
import time
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
import sys
from os import startfile
from multiprocessing import Process

def minute_passed(oldepoch):
    return time.time() - oldepoch >= 60

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GO WALK")
        self.setFixedSize(1920, 1080)
        self.Ui()
        self.show()
        startfile("video.mp4")

    def Ui(self):
        self.setStyleSheet("background-color : black; color : white; font-size: 40px;")
        self.label1 = QLabel("Attention Coder!", self)
        self.label2 = QLabel("You have been on the Pc for a long time", self)
        self.label3 = QLabel("please get up away from the screen", self)
        self.label2.setStyleSheet("color : white;")
        self.label1.move(10, 10)
        self.label1.adjustSize()
        self.label2.move(10, 60)
        self.label2.adjustSize()
        self.label3.move(10, 130)
        self.label3.adjustSize()
        self.showMaximized()


start = time.time()
def main():
    time.sleep(1800)
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
    if minute_passed(start) != True:
        main()


def multi(*functions):
    processes = []
    for function in functions:
        proc = Process(target=function)
        proc.start()
        processes.append(proc)
    for proc in processes:
        proc.join()
while True:
    main()
