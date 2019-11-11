import random
import sys
import threading
import time
import pandas as pd

from PyQt5.QtCore import *
from qtpy import QtWidgets

import ButtonUI.mainwindow
import ButtonUI.start
import ButtonUI.result

app = QtWidgets.QApplication(sys.argv)


def countdown():
    global count
    count = 10
    window.ui.Timer.display(count)
    QCoreApplication.processEvents()
    window.update()
    while count != 0:
        count -= 1
        QCoreApplication.processEvents()
        window.ui.Timer.display(count)
        window.update()
        time.sleep(1)


def randm():
    m = random.randint(1, 9)
    if m == 1:
        window.ui.Lamp1.setChecked(True)
        while True:
            QCoreApplication.processEvents()
            window.update()
            if window.ui.pushButton.isChecked():
                clicked(1)
                break

    if m == 2:
        window.ui.Lamp2.setChecked(True)
        while True:
            QCoreApplication.processEvents()
            window.update()
            if window.ui.pushButton_2.isChecked():
                clicked(2)
                break
    if m == 3:
        window.ui.Lamp3.setChecked(True)
        while True:
            QCoreApplication.processEvents()
            window.update()
            if window.ui.pushButton_3.isChecked():
                clicked(3)
                break
    if m == 4:
        window.ui.Lamp4.setChecked(True)
        while True:
            QCoreApplication.processEvents()
            window.update()
            if window.ui.pushButton_4.isChecked():
                clicked(4)
                break
    if m == 5:
        window.ui.Lamp5.setChecked(True)
        while True:
            QCoreApplication.processEvents()
            window.update()
            if window.ui.pushButton_5.isChecked():
                clicked(5)
                break
    if m == 6:
        window.ui.Lamp6.setChecked(True)
        while True:
            QCoreApplication.processEvents()
            window.update()
            if window.ui.pushButton_6.isChecked():
                clicked(6)
                break
    if m == 7:
        window.ui.Lamp7.setChecked(True)
        while True:
            QCoreApplication.processEvents()
            window.update()
            if window.ui.pushButton_7.isChecked():
                clicked(7)
                break
    if m == 8:
        window.ui.Lamp8.setChecked(True)
        while True:
            QCoreApplication.processEvents()
            window.update()
            if window.ui.pushButton_8.isChecked():
                clicked(8)
                break
    if m == 9:
        window.ui.Lamp9.setChecked(True)
        while True:
            QCoreApplication.processEvents()
            window.update()
            if window.ui.pushButton_9.isChecked():
                clicked(9)
                break


def clicked(nmbr):
    if nmbr == 1:
        window.ui.pushButton.setChecked(False)
        window.ui.Lamp1.setChecked(False)
    if nmbr == 2:
        window.ui.pushButton_2.setChecked(False)
        window.ui.Lamp2.setChecked(False)
    if nmbr == 3:
        window.ui.pushButton_3.setChecked(False)
        window.ui.Lamp3.setChecked(False)
    if nmbr == 4:
        window.ui.pushButton_4.setChecked(False)
        window.ui.Lamp4.setChecked(False)
    if nmbr == 5:
        window.ui.pushButton_5.setChecked(False)
        window.ui.Lamp5.setChecked(False)
    if nmbr == 6:
        window.ui.pushButton_6.setChecked(False)
        window.ui.Lamp6.setChecked(False)
    if nmbr == 7:
        window.ui.pushButton_7.setChecked(False)
        window.ui.Lamp7.setChecked(False)
    if nmbr == 8:
        window.ui.pushButton_8.setChecked(False)
        window.ui.Lamp8.setChecked(False)
    if nmbr == 9:
        window.ui.pushButton_9.setChecked(False)
        window.ui.Lamp9.setChecked(False)


class GameMode1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("IsMirEgal")
        self.ui = ButtonUI.mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.setCheckable(True)
        self.ui.pushButton_2.setCheckable(True)
        self.ui.pushButton_3.setCheckable(True)
        self.ui.pushButton_4.setCheckable(True)
        self.ui.pushButton_5.setCheckable(True)
        self.ui.pushButton_6.setCheckable(True)
        self.ui.pushButton_7.setCheckable(True)
        self.ui.pushButton_8.setCheckable(True)
        self.ui.pushButton_9.setCheckable(True)

        self.ui.pushButton.clicked.connect(lambda: self.ui.pushButton.setChecked(True))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.pushButton_2.setChecked(True))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.pushButton_3.setChecked(True))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.pushButton_4.setChecked(True))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.pushButton_5.setChecked(True))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.pushButton_6.setChecked(True))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.pushButton_7.setChecked(True))
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.pushButton_8.setChecked(True))
        self.ui.pushButton_9.clicked.connect(lambda: self.ui.pushButton_9.setChecked(True))


class NameInput(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Lol")
        self.ui = ButtonUI.start.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(submit)


class result(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("I don't even know what this does")
        self.ui = ButtonUI.result.Ui_MainWindow()
        self.ui.setupUi(self)


def submit():
    global name_input
    global df
    name_input = name.ui.lineEdit.text()
    name.close()
    df = pd.read_csv('scores.csv')
    df = df.append({"Username": name_input,
                    "Score": p}, ignore_index=True)
    df = df.sort_values('Score', ascending=False)
    df.to_csv("./scores.csv", sep=',', index=False)
    resultwindow.ui.label.setText(str(df.head(n=3)))
    resultwindow.show()


name = NameInput()
resultwindow = result()
window = GameMode1()
window.show()

p1 = threading.Thread(target=countdown)
p1.start()

global p
p = 0
while count != 0:
    randm()
    p += 1
    window.ui.Counter.display(p)
window.close()
name.show()

sys.exit(app.exec_())
