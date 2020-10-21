# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_22_su_API_config.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import urllib.request
from PyQt5 import QtCore, QtGui, QtNetwork,QtWidgets
from PyQt5.Qt import QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

import sqlite3
import datetime
import sys

class fci_22_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1331, 711))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(1130, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 70, 1231, 611))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setGeometry(QtCore.QRect(50, 550, 61, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_15.setGeometry(QtCore.QRect(150, 550, 75, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_16.setGeometry(QtCore.QRect(260, 550, 75, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_17.setGeometry(QtCore.QRect(370, 550, 61, 31))
        self.pushButton_17.setObjectName("pushButton_17")
       
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)       
        self.pushButton_19.setGeometry(QtCore.QRect(900, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_18")
        
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        self.label_32.setGeometry(QtCore.QRect(20, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_21.setGeometry(QtCore.QRect(160, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setText("")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_33 = QtWidgets.QLabel(self.groupBox_2)
        self.label_33.setGeometry(QtCore.QRect(20, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox_2)
        self.label_34.setGeometry(QtCore.QRect(20, 220, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(560, 40, 621, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(160, 220, 301, 281))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 110, 291, 81))
        self.textEdit_2.setObjectName("textEdit_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(290, 50, 82, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(390, 50, 82, 31))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_18.setGeometry(QtCore.QRect(470, 550, 61, 31))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_35 = QtWidgets.QLabel(self.groupBox_2)
        self.label_35.setGeometry(QtCore.QRect(570, 550, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(690, 550, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setText("")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(1060, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(1010, 20, 31, 31))
        self.toolButton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
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
        self.label_47.setText(_translate("MainWindow", "05 Aug 2020 14:23:00"))
        self.groupBox_2.setTitle(_translate("MainWindow", "API Config & Test"))
        self.pushButton_14.setText(_translate("MainWindow", "Add"))
        self.pushButton_15.setText(_translate("MainWindow", "Save"))
        self.pushButton_16.setText(_translate("MainWindow", "Delete"))
        self.pushButton_17.setText(_translate("MainWindow", "Reset"))
        self.pushButton_19.setText(_translate("MainWindow", "Return"))
        self.label_32.setText(_translate("MainWindow", "Api Id :"))
        self.label_33.setText(_translate("MainWindow", "Api URL :"))
        self.label_34.setText(_translate("MainWindow", "Json :"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "API ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "API URL"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "JSON"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Method"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Output"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.radioButton.setText(_translate("MainWindow", "Get"))
        self.radioButton_2.setText(_translate("MainWindow", "Post"))
        self.pushButton_18.setText(_translate("MainWindow", "Test"))
        self.label_35.setText(_translate("MainWindow", "Test Output :"))
        self.label_2.setText(_translate("MainWindow", "Internet Message:"))
        self.label_22.setText(_translate("MainWindow", "Internet"))
        self.toolButton.setText(_translate("MainWindow", "On"))
        
        self.pushButton_19.clicked.connect(MainWindow.close)
        
        self.c_select_all_data()
        self.c_rest_fun()
        self.tableWidget.doubleClicked.connect(self.c_fetch_data_from_tw)
        self.pushButton_14.clicked.connect(self.c_add_click) 
        self.pushButton_15.clicked.connect(self.c_edit_click)       
        self.pushButton_16.clicked.connect(self.c_delete_click)
        self.pushButton_17.clicked.connect(self.c_rest_fun)
        self.toolButton.clicked.connect(self.check_internet_connection)
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        self.check_internet_connection()
    def device_date(self):     
        self.label_47.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
       
    
   
    def connect(self):
        try:
            urllib.request.urlopen('http://google.com') #Python 3.x
            return True
        except:
            return False
    
    def check_internet_connection(self):  
        if (self.connect()):
              self.toolButton.setText("On")
              #self.label_22.show()
              self.toolButton.setStyleSheet("background-color: rgb(0, 170, 0);")
    
        else:
              self.toolButton.setText("Off")              
              #self.label_22.show()
              self.toolButton.setStyleSheet("background-color: rgb(170, 0, 0);")
    
      
    
    
    #Contractors            
    def c_fetch_data_from_tw(self):        
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.dr_id=str(self.tableWidget.item(row, 0).text())
            self.lineEdit_21.setText(str(self.tableWidget.item(row, 0).text())) 
            self.textEdit.setText(str(self.tableWidget.item(row, 3).text()))
            self.textEdit_2.setText(str(self.tableWidget.item(row, 2).text()))
            self.api_method='POST'
            print("method :"+str(self.tableWidget.item(row, 1).text()))
            if(self.tableWidget.item(row, 1).text()=='GET'):
                    self.api_method='GET'
                    self.radioButton.setChecked(True)
            else:
                    self.api_method='POST'
                    self.radioButton_2.setChecked(True)
            
            self.pushButton_14.setDisabled(True) #add
            self.pushButton_15.setEnabled(True)  #save
            self.pushButton_16.setEnabled(True) #delete           
            self.pushButton_17.setEnabled(True) #reset
            
        else:    
            self.label_2.setText("Please Select the record.")
            self.label_2.show()
            
           
    def c_rest_fun(self):
        self.lineEdit_21.setText("1")  
        self.textEdit.setText("") 
        self.textEdit_2.setText("")         
        
        self.pushButton_14.setEnabled(True) #add
        self.pushButton_15.setDisabled(True)  #save
        self.pushButton_16.setDisabled(True) #delete           
        self.pushButton_17.setEnabled(True) #reset
        
        self.label_2.hide()
        self.c_select_all_data()        
  
        connection = sqlite3.connect("fci.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'API_MST'")       
        for x in results:           
                 self.lineEdit_21.setText(str(x[0]).zfill(6))            
        connection.close()         
            
   
    def c_load_data(self):        
        if(self.operation_flg=="ADD"):
                #print("inside Add ")
                self.c_add_data()
        elif(self.operation_flg=="EDIT"):
                #print("inside edit ")
                self.c_edit_data()
        elif(self.operation_flg=="DELETE"):
                #print("inside delete ")
                self.c_delete_data()
        else:
                print("Invalid Operation.")
         
    def c_add_click(self):
        self.operation_flg="ADD"       
        self.c_load_data()
        
    def c_add_data(self):
        self.api_method='POST'
        if( self.radioButton.isChecked()):
            self.api_method='GET'
        else:
            self.api_method='POST'
        if(self.lineEdit_21.text() != ""):            
            connection = sqlite3.connect("fci.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO API_MST(API_METHOD,API_JSON,API_URL) VALUES('"+str(self.api_method)+"','"+self.textEdit.toPlainText()+"','"+self.textEdit_2.toPlainText()+"')")                    
            connection.commit();                    
            connection.close()  
      
            self.label_2.setText("Record Added Successfully.")
            self.log_audit("API Config","Added API ID:"+str(self.lineEdit_21.text()))
            self.label_2.show()
        else :
            self.label_2.setText("Id is Empty.")
            self.label_2.show()
            
        self.c_select_all_data()
    
    def c_edit_click(self):
        self.api_method='POST'
        if( self.radioButton.isChecked()):
            self.api_method='GET'
        else:
            self.api_method='POST'
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="EDIT"
            self.c_load_data()
        else:    
            self.label_2.setText("Contractor:Please Select the record.")
            self.label_2.show() 
    
    def c_edit_data(self):
        if(self.lineEdit_21.text() != ""):
            connection = sqlite3.connect("fci.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE API_MST SET API_METHOD='"+str(self.api_method)+"',API_JSON='"+self.textEdit.toPlainText()+"',API_URL='"+self.textEdit_2.toPlainText()+"' WHERE  API_ID ='"+str(self.dr_id)+"'")                    
            connection.commit();                    
            connection.close()   
       
        self.label_2.setText("Record Saved Successfully.")
        self.log_audit("API Config","Edited API ID:"+str(self.lineEdit_21.text()))
        self.label_2.show()
        self.c_select_all_data()
    
    def c_delete_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="DELETE"
            self.c_load_data()
        else:    
            self.label_2.setText("Contractor:Please Select the record.")
            self.label_2.show()        
     
      
    def c_delete_data(self):
        close = QMessageBox()
        close.setText("This would remove important data from system.Are You Sure Want to Delete ? ")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:
            if(self.lineEdit_21.text() != ""):
                connection = sqlite3.connect("fci.db")
                with connection:        
                        cursor = connection.cursor()
                        cursor.execute("DELETE FROM API_MST WHERE API_ID ='"+str(self.dr_id)+"'")                    
                connection.commit();                    
                connection.close()
                
                self.label_2.setText("Record Deleted Successfully.")
                self.log_audit("API Config","Deleted API ID:"+str(self.lineEdit_21.text()))
                self.label_2.show()
                
                self.c_select_all_data()
        else:
            self.label_2.setText("Cancled Delete API.")
            self.label_2.show()   
            
         
    def c_select_all_data(self):     
        self.c_delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
      
        self.tableWidget.setHorizontalHeaderLabels(['Api ID.','Method', ' Api Url ','JSON', 'Status','OutPut'] )       
           
        connection = sqlite3.connect("fci.db")
        results=connection.execute("select API_ID,API_METHOD,API_URL,API_JSON ,'','' FROM API_MST")                        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))                
        connection.close()   
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
    
    def c_delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)        
            
        
    
    def log_audit(self,event_name,desc_str):        
        connection = sqlite3.connect("fci.db")
        with connection:        
            cursor = connection.cursor()       
            cursor.execute("INSERT INTO AUDIT_MST(AUDIT_TYPE,MESSAGE) VALUES(?,?)",(event_name,desc_str))
            cursor.execute("UPDATE AUDIT_MST SET USER_ID = (SELECT LOGIN_USER_ID FROM GLOBAL_VAR) WHERE USER_ID IS NULL")            
        connection.commit();
        connection.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_22_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
