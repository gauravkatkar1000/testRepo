# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_01_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import urllib.request
from PyQt5 import QtCore, QtGui,QtNetwork, QtWidgets
import sqlite3
import datetime
import sys,os
import time
from PyQt5.QtCore import QDate
import sys,os

from fci_02_Batches import fci_02_Ui_MainWindow
from fci_05_Issues import fci_05_Ui_MainWindow
from fci_08_reports_submenu import fci_08_Ui_MainWindow
from fci_13_admin_submenu import fci_13_Ui_MainWindow
from fci_04_batch_issues_submenu import fci_04_Ui_MainWindow

from fci_29_stacks import fci_29_Ui_MainWindow


class fci_01_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(25, 25, 1291, 718))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet("background-color: rgb(47, 141, 255);")
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 180, 211, 121))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 200, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 400, 211, 121))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 200, 158);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 180, 211, 121))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 200, 158);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(290, 30, 721, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(1060, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setPointSize(12)        
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        
        self.label_20_1 = QtWidgets.QLabel(self.frame)
        self.label_20_1.setGeometry(QtCore.QRect(300, 100, 721, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)        
        self.label_20_1.setFont(font)
        self.label_20_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20_1.setObjectName("label_20_1")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 600, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(910, 600, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        #self.pushButton_5.setStyleSheet("background-color: rgb(255, 200, 158);")
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.pushButton_5_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5_1.setGeometry(QtCore.QRect(610, 600, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5_1.setFont(font)
        self.pushButton_5_1.setObjectName("pushButton_5_1")
        
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(1060, 590, 250, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(110, 400, 211, 121))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 200, 158);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(870, 180, 211, 121))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 200, 158);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(490, 400, 211, 121))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 200, 158);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(20, 20, 51, 41))
        self.toolButton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(80, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.device_location_type = ""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", " Weighing"))
        self.pushButton_3.setText(_translate("MainWindow", "Admin."))
        self.pushButton_4.setText(_translate("MainWindow", "Recipts "))
        self.label.setText(_translate("MainWindow", "HI-TECH MATERIAL HANDLING SYSTEM"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45 "))
        self.label_20_1.setText(_translate("MainWindow", "LoginBy: Sanjaykumar Mane (Super Admin) "))
        self.pushButton_2.setText(_translate("MainWindow", "Shutdown"))
        self.pushButton_5.setText(_translate("MainWindow", "Reboot"))
        self.pushButton_5_1.setText(_translate("MainWindow", "SignOut"))
        self.label_21.setText(_translate("MainWindow", "AnyDesk Id: 456533323"))
        self.pushButton_6.setText(_translate("MainWindow", "Reports"))
        self.pushButton_7.setText(_translate("MainWindow", "Issues"))
        
        self.pushButton_9.setText(_translate("MainWindow", "Stacks"))
        
        self.label_22.setText(_translate("MainWindow", "Internet"))
        self.toolButton.setText(_translate("MainWindow", "On"))        
        self.pushButton_5_1.clicked.connect(MainWindow.close)
        self.startx()



    def startx(self): 
        self.anydesk_open()
        self.pushButton.clicked.connect(self.open_new_window)
        self.pushButton_4.clicked.connect(self.open_new_window2)
        self.pushButton_7.clicked.connect(self.open_new_window4)
        self.pushButton_6.clicked.connect(self.open_new_window5)
        self.pushButton_3.clicked.connect(self.open_new_window6)
        self.pushButton_9.clicked.connect(self.open_new_window7)
        self.pushButton_2.clicked.connect(self.shutdown_system)
        self.pushButton_5.clicked.connect(self.reboot_system)
        
        self.toolButton.clicked.connect(self.check_internet_connection)
        self.check_internet_connection()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        connection = sqlite3.connect("fci.db")
        results=connection.execute("SELECT LOGIN_USER_NAME,DEVICE_LOCATION_TYPE  FROM GLOBAL_VAR") 
        for x in results:
            self.label_20_1.setText("Logged In : "+str(x[0])+" @ "+str(x[1]))
            self.device_location_type=str(x[1])
        connection.close()
        
        if(str(self.device_location_type) == 'SITE'):
             #self.label.setText("Material Handling and Transport System 1.0 \n @ Site")
             self.pushButton_7.setDisabled(True)
             self.pushButton_9.setDisabled(True)
        else:
            #self.label.setText("Material Handling and Transport System 1.0 \n @ Storage")
            self.pushButton_7.setEnabled(True)
            self.pushButton_9.setEnabled(True)
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
     
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
    
    
    def shutdown_system(self):
        self.log_audit("Login","SignOut From System.")
        os.system("sudo shutdown -P 0")
        
    def reboot_system(self):
        self.log_audit("Login","SignOut From System.")
        os.system("sudo reboot")
    
    def closeEvent(self,event):
        self.log_audit("Login","SignOut From System-close_event.")
        print("closed window")        
        #self.event.accept()
        #quit.triggered.connect(self.close)
    
    
    
    def anydesk_open(self):
        self.anydesk_id =0
        os.system("rm -rf anydes_id_f.txt")
        os.system("anydesk --get-id >> anydes_id_f.txt")
        f = open('anydes_id_f.txt','r')
        for line in f:                 
                    self.anydesk_id = line[0:9]
        print("self.anydesk_id:"+str(self.anydesk_id))
        self.label_21.setText("AnyDesk ID:"+str(self.anydesk_id))
        f.close()
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))

    def open_new_window(self):                
        f = open("/var/local/devid", "r")
        dev_id=f.read()
        f.close()
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("services.db")
        results=connection.execute("select DEVICE_SERIAL_NO from DAT_MST") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))
           if(serial_no == str(x[0])):
               self.go_ahead="Yes"
           else:
               self.go_ahead="No"
        connection.close()
        
        if(self.go_ahead=="Yes"):       
            if(dev_id=='201910:0003'):            
                connection = sqlite3.connect("services.db")
                results=connection.execute("select DAT_STR from DAT_MST") 
                for x in results:
                    #print("DATE Str :"+str(x[0]))
                    DAT_DT=datetime.datetime.strptime(str(x[0]),"%Y-%m-%d").date()
                    CURR_DT=datetime.date.today()               
                    
                    #print("date dt :"+str(DAT_DT))
                    #print("curr dt :"+str(CURR_DT))                
                    if(DAT_DT > CURR_DT):                         
                             self.window = QtWidgets.QMainWindow()
                             self.ui=fci_04_Ui_MainWindow()
                             self.ui.setupUi(self.window)           
                             self.window.show()
                             
                    else:
                        print("DAT date problem.")
                connection.close()         
            else:
                print("dev id :"+str(dev_id))
        else:
           print("Device Invalid :"+str(serial_no))
     
            
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_02_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()   
        
   
    def open_new_window4(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_05_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()     
    
    def open_new_window5(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_08_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window6(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_13_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window7(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_29_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window8(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_32_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def getserial(self):
        # Extract serial from cpuinfo file
        cpuserial = "0000000000000000"
        try:
           f = open('/proc/cpuinfo','r')
           for line in f:
                if line[0:6]=='Serial':
                   cpuserial = line[10:26]
           f.close()
        except:
           cpuserial = "ERROR000000000"
        return cpuserial
    
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
    ui = fci_01_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
