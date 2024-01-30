# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coomd.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton
from hii import Ui_Hii
from tab1 import Ui_Tab1

import sqlite3

cmd_list=['-','-']
process_list=['-','-']
epaisseur_list=[1.9,2.7]
largeur_list=[1250,1110]
dic_ep=dict()

dic_ep['0.24<<0.4']='1.8<<2'

dic_ep['0.33<<0.6']='2<<2.2'

dic_lg=dict()

dic_lg['910<<912']='935<<940'

dic_lg['980']='1005<<1010'

class Ui_Cm(object):
    def loaddata(self):
        connection = sqlite3.connect('dbbase.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Commande'

        tablerow=0
        results = cur.execute(sqlstr)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(results):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))
        
        for row in range(self.tableWidget.rowCount()):
                    button = QPushButton('Cliquez ici')
                    self.tableWidget.setCellWidget(row, 5, button)
                    button.clicked.connect(lambda _,r=row:self.nextpage(r))

    def nextpage(self,row):
         #recuperation la largeur
         #recuperation l'epaisseur
         #condition if
         epaisseur=self.tableWidget.item(int(row), 3).text()
         largeur=self.tableWidget.item(int(row), 4 ).text()
         process=self.tableWidget.item(int(row), 2).text()
         print (row)


         
         self.MainWindow = QtWidgets.QMainWindow()

         self.ui = Ui_Hii()
         self.ui.setupUi(self.MainWindow,epaisseur,largeur,process)
         #self.ui.next(row,process,epaisseur,largeur)
         self.MainWindow.show()







         








      




             
     

         


    



    
            

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 12, 320, 80))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 100, 700, 350))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 800, 70, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loaddata)

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        for row in range(self.tableWidget.rowCount()):
            button = QPushButton('Cliquez ici')
            self.tableWidget.setCellWidget(row, 5, button)
           

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "Commande"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Num cmd"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type cmd"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "process"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "epaisseur"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "largeur"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "submit"))
        self.pushButton.setText(_translate("MainWindow", "load"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Cm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
