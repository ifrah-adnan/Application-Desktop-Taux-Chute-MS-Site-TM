# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Dell Latitude 5420\OneDrive\Bureau\phase_3\soo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1313, 807)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1341, 941))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(20, 20, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.widget.setFont(font)
        self.widget.setStyleSheet("border-image: url(:/img/Logo_-_Maghreb_Steel_(1).jpg);\n"
"border-radius:50px;")
        self.widget.setObjectName("widget")
        self.main1 = QtWidgets.QWidget(self.frame)
        self.main1.setGeometry(QtCore.QRect(0, 80, 781, 631))
        self.main1.setMinimumSize(QtCore.QSize(0, 381))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.main1.setFont(font)
        self.main1.setStyleSheet("border-image: url(:/img/mains.jpeg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(10, 120, 178, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:50px;")
        self.main1.setObjectName("main1")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(810, 90, 481, 631))
        self.label.setStyleSheet("background-color: rgb(88, 161, 200);\n"
"border-radius:50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_4.setGeometry(QtCore.QRect(1090, 210, 151, 151))
        self.textEdit_4.setStyleSheet("border-image: url(:/img/ccccc.jpg);\n"
"border-radius:50px;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_5.setGeometry(QtCore.QRect(1080, 420, 161, 181))
        self.textEdit_5.setStyleSheet("border-image: url(:/img/stock.png);\n"
"border-radius:50px;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 470, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(200, 170, 62);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(880, 250, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(200, 170, 62);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Stock"))
        self.pushButton.setText(_translate("MainWindow", "Commande"))
import res_rc
