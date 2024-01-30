from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_St(object):
    

    def loaddata(self):
        connection = sqlite3.connect('dbbase.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM stock'

        tablerow=0
        results = cur.execute(sqlstr)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(results):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 12, 201, 48))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 70, 700, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(60, 800, 70, 30))
        self.btn_next.setObjectName("btn_next")
        self.pushButton_ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_.setGeometry(QtCore.QRect(180, 800, 70, 30))
        self.pushButton_.setObjectName("pushButton_")
        self.pushButton_.clicked.connect(self.loaddata)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 800, 70, 30))
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 18))
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
        self.lineEdit.setText(_translate("MainWindow", " Stock"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Process"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Epaisseur"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Largeur"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Poids"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Grade"))
        self.btn_next.setText(_translate("MainWindow", "Back"))
        self.pushButton_.setText(_translate("MainWindow", "Load"))
        self.pushButton.setText(_translate("MainWindow", "Check"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_St()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
