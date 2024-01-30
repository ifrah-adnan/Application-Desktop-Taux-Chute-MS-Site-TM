# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hola.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt,QDateTime
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

dic_ep=dict()

dic_ep['0.24<<0.4']='1.8<<2'
dic_ep['0.33<<0.6']='2<<2.2'
dic_ep['0.45<<0.9']='2.2<<2.4'
dic_ep['0.6<<1.2']='2.4<<2.7'
dic_ep['0.7<<1.3']='2.7<<3'
dic_ep['1<<1.6']='3<<3.4'
dic_ep['1.4<<1.75']='3.4<<3.6'
dic_ep['1.6<<4']='3.6<<8'





#----------------------------------------------------------

dic_lg=dict()

dic_lg['910_912']='935<<940'
dic_lg['980']='1005<<1010'
dic_lg['1000']='1025<<1030'
dic_lg['1059_1060_1065']='1090'
dic_lg['1070']='1095<<1100'
dic_lg['1100']='1125<<1130'
dic_lg['1160_1165']='1190'
dic_lg['1200']='1225<<1230'
dic_lg['1206']='1240'
dic_lg['1210']='1235<<1240'
dic_lg['1219_1220']='1245<<1250'
dic_lg['1250']='1275<<1280'
dic_lg['1260']='1285<<1290'
dic_lg['1294']='1320'



dic_pro =dict()
dic_pro["LAC"]=["PK"]
dic_pro["GAL"]=["PK","CRMA","LGA"]
dic_pro["PPO"]=["PK","CRMA","LGA"]
dic_pro["LAF"]=["PK","CRMB","BAF","SKP"]
dic_pro["CA"]=["PK","CRMA","LGB"]

#----------------------
di=dict()
di['PK']='0-6'
di['CRMA']='0-3'
di['LGA']='0-2.5'
di['CRMB']='0-2.5'
di['LGB']='0-2.5'
di['BAF']='0'
di['SKP']='0-2'





connection = sqlite3.connect('dbbase.db')
cur = connection.cursor()
class Ui_Cm(object):

    
    def loaddata(self,row):
        
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
        row_count = self.tableWidget.rowCount()
        column_count = self.tableWidget.columnCount()
        for row in range(row_count):
            for column in range(column_count):
                item = self.tableWidget.item(row, column)
                if item is not None and item.text() == "None":
                    self.tableWidget.setItem(row, column, QTableWidgetItem(""))
                
                
        
        for row in range(self.tableWidget.rowCount()):
                    button = QPushButton('Cliquez ici')
                    self.tableWidget.setCellWidget(row, 10, button)
                    button.clicked.connect(lambda _,r=row:self.nextpage(r))
                    button.clicked.connect(lambda checked, r=row: self.on_button_clicked(r))
     
                    button.clicked.connect(lambda checked, r=row: self.date(r))
                    button.clicked.connect(lambda checked, r=row: self.result(r))

    
    def date (self,row):
        connection = sqlite3.connect('dbbase.db')
        cur = connection.cursor()
        date = QDateTime.currentDateTime()
        date_string = date.toString(Qt.ISODate)
        item = QTableWidgetItem(date_string)
        self.tableWidget.setItem(row, 8, item)
        mydate = self.tableWidget.setItem(row, 8, item)


        cur.execute("UPDATE Commande SET date = ? WHERE NumC = ?", (date_string, row+1))
        connection.commit()

    def result(self, row):
        connection = sqlite3.connect('dbbase.db')
        cur = connection.cursor()
        res = int(self.tableWidget.item(int(row), 7).text())
        row_count = self.tableWidget2.rowCount()
        
        if res > row_count:
                
                item = QTableWidgetItem(str("non disponible"))
                self.tableWidget.setItem(row, 9, item)
                msg="non diponible"
                cur.execute("UPDATE Commande SET resultat = ? WHERE NumC = ?", (msg, row+1))
                connection.commit()


        else:
                items = QTableWidgetItem(str(" disponible"))

                self.tableWidget.setItem(row, 9, items)
                msgg="disponible"
                cur.execute("UPDATE Commande SET resultat = ? WHERE NumC = ?", (msgg, row+1))
                connection.commit()



       

                  






     

                    






    def on_button_clicked(self, row):
        connection = sqlite3.connect('dbbase.db')
        cur = connection.cursor()
        status_item = self.tableWidget.item(row, 6)
        status = status_item.text()

        if status == "Cliqué":
            # La ligne a déjà été cliquée, effectuer une action appropriée
            print(f"Ligne {row} déjà cliquée!")
        else:
            # Marquer la ligne comme cliquée dans le widget de tableau
            status_item.setText("deja consulté")

        
        message =  ' deja consulte'
        cur.execute("UPDATE Commande SET status = ? WHERE NumC = ?", (message, row+1))
        connection.commit()
        
        
            
    


    def nextpage(self,row):
         #recuperation la largeur
         #recuperation l'epaisseur
         #condition if

          epaisseur=self.tableWidget.item(int(row), 3).text()
          largeur=self.tableWidget.item(int(row), 4 ).text()
          process=self.tableWidget.item(int(row), 2).text()
          num=self.tableWidget.item(int(row), 0).text()
          
          ep_stock=[]
          for key in dic_ep.keys():
              if '<<' in key:
                   lst=key.split('<<')
                   if float(lst[0])<=float(epaisseur)<=float(lst[1]):
                        print(dic_ep[key])

                        ep_stock.append(dic_ep[key])

              else:
                   if float(key)==float(epaisseur):
                        ep_stock.append(dic_ep[key])

                        print(dic_ep[key])
          for key in dic_lg.keys():
              if '_' in key:
                   lst=key.split('_')
                  
                   for lg in lst:
                        if float(lg)==float(largeur):
                             lg_stock=dic_lg[key]
                             break

               

              else:
                   if float(key)==float(largeur):
                        lg_stock=dic_lg[key]
                        print(dic_lg[key])                
       
        
                     
        
        
          if '<<' in lg_stock:
              lst=lg_stock.split('<<')
              lg_inferieur=lst[0]
              lg_superieur=lst[1]
              print (lg_inferieur)
              print(lg_superieur)
          else:
             lg_inferieur=lg_stock
             lg_superieur=lg_stock
             
          self.tableWidget2.setRowCount(0)
          for ep_interv in ep_stock:     
            if '<<' in ep_interv:
                lst=ep_interv.split('<<')
                ep_inferieur=lst[0]
                ep_superieur=lst[1]
                print (ep_inferieur)
                print(ep_superieur)      

                query="select * from stock where epaisseur >='"+ep_inferieur+"'and epaisseur<='"+ep_superieur + "' and largeur>='"+lg_inferieur+"'and largeur<='"+lg_superieur+"'"
                tablerow=0
                results = cur.execute(query)
                ii=0
                for row_number, row_data in enumerate(results):
                    ii=ii+1
                    self.tableWidget2.insertRow(row_number)
                    for column_number,data in enumerate(row_data):
                
                      self.tableWidget2.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))
                

                 
                for row in range(self.tableWidget2.rowCount()):
                    button = QPushButton('Cliquez ici')
                    self.tableWidget2.setCellWidget(row, 6, button)
                  
                    infos=[row,process,epaisseur,largeur,num]
                    button.clicked.connect(lambda _,r=infos:self.next(r))
                    button.clicked.connect(lambda _,r=infos:self.on_button(r))

                    

        
                
                 


                    

                    
     
       
             
         
        

          if self.tableWidget2.rowCount()==0:
           # app = QApplication(sys.argv)
            self.show_messagebox()


            


        

            
    def on_button(self, infos):
        row=infos[0]
        process=infos[1]
        epaisseur_comm=infos[2]
        largeur_comm=infos[3]
        num=infos[4]


        connection = sqlite3.connect('dbbase.db')
        cur = connection.cursor()

        status_item = self.tableWidget2.item(row, 5)
        status = status_item.text()

        if status == "deja consulte":
            # La ligne a déjà été cliquée, effectuer une action appropriée
            print(f"Ligne {row} déjà cliquée!")
        else:
            # Marquer la ligne comme cliquée dans le widget de tableau
            status_item.setText("deja reserve")

    
                  
        ID=self.tableWidget2.item(int(row), 0).text()
       

        
        message =  ' deja reserve pour la commande  {}'.format(num)
        cur.execute("UPDATE stock SET status = ? WHERE ID = ?", (message, ID))
        connection.commit()       

            # Afficher la table widget
    def show_messagebox(self):
        # Créer un QMessageBox avec un message et un bouton "OK"
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Critical)
        messageBox.setStandardButtons(QMessageBox.Ok)




        messageBox.setText("À produire")
        messageBox.setWindowTitle("Message")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.resize(400, 300)  # définit la taille de la boîte de dialogue
        messageBox.exec_()
        
    

    def next(self,infos):
          print(infos,"  :this is infos") 
         
          row=infos[0]
          process=infos[1]
          epaisseur_comm=infos[2]
          largeur_comm=infos[3]
          epaisseur_st=self.tableWidget2.item(int(row), 1).text()
          largeur_st=self.tableWidget2.item(int(row),  2).text()
          

          list_process=dic_pro[process]

          self.tableWidget_3.setRowCount(0)
          for i in range(len(list_process)):
            self.tableWidget_3.insertRow(i)
            self.tableWidget_3.setItem(i, 0,QtWidgets.QTableWidgetItem(str(list_process[i])))
            self.tableWidget_3.setItem(i, 3,QtWidgets.QTableWidgetItem(str(di[list_process[i]])))

           
            if list_process[i]=="PK":
                self.tableWidget_3.setItem(i, 1,QtWidgets.QTableWidgetItem(str(epaisseur_st)))
                self.tableWidget_3.setItem(i, 2,QtWidgets.QTableWidgetItem(str(largeur_comm)))
            else:
                self.tableWidget_3.setItem(i, 1,QtWidgets.QTableWidgetItem(str(epaisseur_comm)))
                self.tableWidget_3.setItem(i, 2,QtWidgets.QTableWidgetItem(str(largeur_comm)))

          print("CLICKED")
         
          print(list_process) 

   



            

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 621)
        font = QtGui.QFont()
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 180, 1000, 370))
        self.tableWidget.setStyleSheet("background-color: rgb(213, 213, 255);\n"
"font: 75 8pt \"Verdana\";\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)

        self.tableWidget2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget2.setGeometry(QtCore.QRect(1100, 180, 800, 350))
        self.tableWidget2.setStyleSheet("background-color: rgb(213, 213, 255);\n"
    "font: 75 8pt \"Verdana\";\n"
    "")
        self.tableWidget2.setObjectName("tableWidget")
        self.tableWidget2.setColumnCount(7)
        self.tableWidget2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(6, item)
        
        

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 550, 150, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(190, 176, 217, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-right-color: rgb(229, 202, 255);\n"
"border-bottom-color: rgb(158, 158, 255);\n"
"border-radius:30px;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 401, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(190, 176, 217, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1100, 100, 401, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(190, 176, 217, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 0, 300, 50))
        self.textEdit.setStyleSheet("border-image: url(:/images/Logo_-_Maghreb_Steel_(1).jpg);")
        self.textEdit.setObjectName("textEdit")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(500, 600,800 ,350 ))
        self.tableWidget_3.setStyleSheet("background-color: rgb(213, 213, 255);\n"
"font: 75 8pt \"Verdana\";\n"
"")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
  

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.pushButton_2.clicked.connect(self.loaddata)
        


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My APP"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Num Cmd"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type cmd"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "process"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "epaisseur"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "largeur"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Poids"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Statut"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Quantitè"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Resultat"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Submit"))


        item = self.tableWidget2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))

        item = self.tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Epaisseur"))
        item = self.tableWidget2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Largeur"))
        item = self.tableWidget2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Poids"))
        item = self.tableWidget2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Grade"))
        item = self.tableWidget2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Statut"))
        item = self.tableWidget2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Submit"))


        self.pushButton_2.setText(_translate("MainWindow", "Load"))
        self.label.setText(_translate("MainWindow", " Commande"))
        self.label_2.setText(_translate("MainWindow", "Stock"))
        
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Process"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Epaisseur"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Largeur"))
      
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Taux de chute %"))

        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

        import resource_rc 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Cm()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
