# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ButtonUI\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 832)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 340, 75, 23))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 340, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 340, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.Lamp1 = QtWidgets.QCheckBox(self.centralwidget)
        self.Lamp1.setGeometry(QtCore.QRect(145, 300, 70, 17))
        self.Lamp1.setObjectName("Lamp1")
        self.Lamp2 = QtWidgets.QCheckBox(self.centralwidget)
        self.Lamp2.setGeometry(QtCore.QRect(315, 300, 70, 17))
        self.Lamp2.setObjectName("Lamp2")
        self.Lamp3 = QtWidgets.QCheckBox(self.centralwidget)
        self.Lamp3.setGeometry(QtCore.QRect(485, 300, 70, 17))
        self.Lamp3.setObjectName("Lamp3")
        self.Counter = QtWidgets.QLCDNumber(self.centralwidget)
        self.Counter.setGeometry(QtCore.QRect(90, 130, 191, 91))
        self.Counter.setSmallDecimalPoint(False)
        self.Counter.setProperty("intValue", 0)
        self.Counter.setObjectName("Counter")
        self.Timer = QtWidgets.QLCDNumber(self.centralwidget)
        self.Timer.setGeometry(QtCore.QRect(440, 130, 191, 91))
        self.Timer.setObjectName("Timer")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(310, 590, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(480, 590, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.Lamp9 = QtWidgets.QCheckBox(self.centralwidget)
        self.Lamp9.setGeometry(QtCore.QRect(485, 550, 70, 17))
        self.Lamp9.setObjectName("Lamp9")
        self.Lamp7 = QtWidgets.QCheckBox(self.centralwidget)
        self.Lamp7.setGeometry(QtCore.QRect(145, 550, 70, 17))
        self.Lamp7.setObjectName("Lamp7")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(140, 590, 75, 23))
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.Lamp8 = QtWidgets.QCheckBox(self.centralwidget)
        self.Lamp8.setGeometry(QtCore.QRect(315, 550, 70, 17))
        self.Lamp8.setObjectName("Lamp8")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 480, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 480, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.Lamp6 = QtWidgets.QCheckBox(self.centralwidget)
        self.Lamp6.setGeometry(QtCore.QRect(485, 440, 70, 17))
        self.Lamp6.setObjectName("Lamp6")
        self.Lamp4 = QtWidgets.QCheckBox(self.centralwidget)
        self.Lamp4.setGeometry(QtCore.QRect(145, 440, 70, 17))
        self.Lamp4.setObjectName("Lamp4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 480, 75, 23))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.Lamp5 = QtWidgets.QCheckBox(self.centralwidget)
        self.Lamp5.setGeometry(QtCore.QRect(315, 440, 70, 17))
        self.Lamp5.setObjectName("Lamp5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 60, 111, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 60, 111, 51))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Click"))
        self.pushButton_2.setText(_translate("MainWindow", "Click"))
        self.pushButton_3.setText(_translate("MainWindow", "Click"))
        self.Lamp1.setText(_translate("MainWindow", "Lamp1"))
        self.Lamp2.setText(_translate("MainWindow", "Lamp2"))
        self.Lamp3.setText(_translate("MainWindow", "Lamp3"))
        self.pushButton_8.setText(_translate("MainWindow", "Click"))
        self.pushButton_9.setText(_translate("MainWindow", "Click"))
        self.Lamp9.setText(_translate("MainWindow", "Lamp9"))
        self.Lamp7.setText(_translate("MainWindow", "Lamp7"))
        self.pushButton_7.setText(_translate("MainWindow", "Click"))
        self.Lamp8.setText(_translate("MainWindow", "Lamp8"))
        self.pushButton_5.setText(_translate("MainWindow", "Click"))
        self.pushButton_6.setText(_translate("MainWindow", "Click"))
        self.Lamp6.setText(_translate("MainWindow", "Lamp6"))
        self.Lamp4.setText(_translate("MainWindow", "Lamp4"))
        self.pushButton_4.setText(_translate("MainWindow", "Click"))
        self.Lamp5.setText(_translate("MainWindow", "Lamp5"))
        self.label.setText(_translate("MainWindow", "Score:"))
        self.label_2.setText(_translate("MainWindow", "Remaining time:"))