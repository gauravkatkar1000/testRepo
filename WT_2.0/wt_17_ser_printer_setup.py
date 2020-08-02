# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_17_ser_printer_setup.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from cryptography.fernet import Fernet
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3

class wt_17_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 701)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1121, 611))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(40, 40, 451, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(460, 60, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(230, 130, 631, 131))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 141, 31))
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(210, 50, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 50, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 50, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(830, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(110, 280, 921, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 320, 901, 241))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(390, 50, 121, 41))
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(540, 50, 211, 41))
        self.comboBox.setObjectName("comboBox")
        
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(160, 50, 171, 41))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 120, 211, 41))
        self.radioButton_2.setObjectName("radioButton_2")
        
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(390, 120, 121, 41))
        self.label_9.setObjectName("label_9")
        self.label_9.setText("Note on Print:")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(520, 130, 348, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 21))
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
        self.label_19.setText(_translate("MainWindow", "Printer Setup"))
        self.label_3.setText(_translate("MainWindow", "Incorrect Password."))
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Printer Details"))
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
        self.label_8.setText(_translate("MainWindow", "Printer Model :"))
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, _translate("MainWindow", "Epson"))
        self.comboBox.setItemText(1, _translate("MainWindow", "HP"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Canon"))
        self.radioButton.setText(_translate("MainWindow", "Plain Paper"))
        self.radioButton_2.setText(_translate("MainWindow", "Pre-Printed Page"))
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.login_page)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.label_3.hide()        
        self.groupBox_2.hide()
        self.pushButton_2.clicked.connect(self.reset_loging)
        ###
        #self.pushButton_6.clicked.connect(self.reset_fun)
        self.pushButton_5.clicked.connect(self.save_data)
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def login_page(self):
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PWD,xxx FROM SERVICES_MST WHERE SERVICE_NAME = 'PRINTER_SETUP' AND STATUS = 'ACTIVE'") 
        for x in results:
            print("key:"+str(x[1]))
            key=str(x[1])
            val=str(x[0])
            val2=str.encode(val)
            #val2=bytes(x[0],'utf-8')
            #print("pwd:"+str(x[0]))
            d_cipher_suite = Fernet(str(x[1]))
            #print("type:"+str(type(val2)))
            plain_text = d_cipher_suite.decrypt(val2)
            #print("plain_text :"+str(plain_text,'utf-8'))
           
            if(str(self.lineEdit.text()) == str(plain_text,'utf-8')):                     
                self.go_ahead_flg="No"
                self.groupBox_2.show()
                self.load_data()
            else:
                self.label_3.show()   
                self.groupBox_2.hide()                 
        connection.close()    
    
    def reset_loging(self):
        self.lineEdit.setText("")
        self.label_3.hide()
        self.groupBox_2.hide()
       
    def load_data(self):
        self.i=0
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PRE_PRINT_FLAG, PRINTER_NAME,PRINT_NOTE FROM DEVICE_CONF ") 
        for x in results:            
            if(str(x[0]) == 'ACTIVE'):
                self.radioButton_2.setChecked(True)
                self.radioButton.setChecked(False)
            else:
                self.radioButton.setChecked(True)
                self.radioButton_2.setChecked(False)
                
            self.comboBox.setCurrentText(str(x[1]))
            self.textEdit.setText(str(x[2])) 
        connection.close()
        
        
        
        
        
        self.label_3.hide() 
    
    def reset_fun(self):
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")   
        self.label_3.hide()  
    
            
    def save_data(self):
        if(self.radioButton_2.isChecked()):
            self.pre_print="ACTIVE"
        else:
            self.pre_print="DEACTIVE"
        
                  
        connection = sqlite3.connect("services.db")          
        with connection:        
                cursor = connection.cursor()                    
                cursor.execute("UPDATE DEVICE_CONF SET PRE_PRINT_FLAG = '"+str(self.pre_print)+"', PRINTER_NAME='"+str(self.comboBox.currentText())+"', PRINT_NOTE='"+self.textEdit.toPlainText()+"'") 
        connection.commit();
        connection.close()
        
        self.label_3.setText(" Saved.") 
        self.label_3.show()                  
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_17_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
