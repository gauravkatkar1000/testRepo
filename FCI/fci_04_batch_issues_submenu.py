# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_04_batch_issues_submenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from fci_03b_weighing_storage_batch import fci_03b_Ui_MainWindow
from fci_03i_weighing_storage_issues import fci_03i_Ui_MainWindow
from fci_03_weighing import fci_03_Ui_MainWindow
from fci_34_weighing_others import fci_34_Ui_MainWindow
from fci_01_main import fci_01_Ui_MainWindow

from fci_39_dup_issues_storage import fci_39_Ui_MainWindow
from fci_40_dup_recipt_storage import fci_40_Ui_MainWindow
from fci_41_dup_recipt_site import fci_41_Ui_MainWindow
from fci_42_dup_other_weighing import fci_42_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import re
import os,sys
import serial,time


class fci_04_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color: rgb(47, 141, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 10, 1311, 711))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("color: rgb(255, 255, 255);\n")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(560, 440, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(50, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 620, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 620, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 120, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 620, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n background-color: rgb(0, 0, 130);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(50, 90, 1141, 321))
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setStyleSheet("color: rgb(255, 0, 0);\n background-color: rgb(0, 0, 0);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(4)
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_53 = QtWidgets.QLabel(self.frame)
        self.label_53.setGeometry(QtCore.QRect(1200, 340, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_53.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_53.setObjectName("label_53")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 620, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(410, 20, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(630, 510, 20, 101))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(110, 520, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0, 0, 255);")
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(330, 520, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_4.setIconSize(QtCore.QSize(16, 16))
        self.radioButton_4.setAutoRepeat(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)
        self.lineEdit.setValidator(input_validator)
        
        self.lineEdit.setGeometry(QtCore.QRect(760, 530, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 440, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(0, 120, 0);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(950, 440, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(0, 120, 0);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(970, 530, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(1180, 620, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color: rgb(255, 255, 255);\n background-color: rgb(0, 0, 130);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(1120, 530, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 120, 0);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(760, 620, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(1200, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.new_slip_flag="HIDE"
        self.old_slip_flag="HIDE"
        self.slip_status=""
        self.command_str=""
        self.ser=""
        self.gross_tare_flag=""
        self.old_slip_no=""       
        self.IO_error_flg=0
        self.line = ""
       
        self.xstr0=""
        self.xstr1=""
        self.xstr2=""
        self.xstr4=""
        self.buff=[]
        self.serial_no=""
        self.batch_id=0
        self.issue_id=0
        self.dev_loc_type=""
        self.status=""
        
        self.last_value=0
        self.current_value=0
        self.enable_buttons_flag="No"
        self.enable_counter=0
        self.weighing_crosses_min_wt_lim="No"
        self.wt_min_limit=0
        self.wt_max_limit=0
        
        self.green_counter=0
        self.ld_set=0
        self.last_display_val=""
       

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ZERO"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00"))
        self.pushButton_3.setText(_translate("MainWindow", "RECIPT"))
        self.pushButton_4.setText(_translate("MainWindow", "ISSUE"))
        self.pushButton_5.setText(_translate("MainWindow", "OTHER"))
        self.label_53.setText(_translate("MainWindow", "Kg."))
        self.pushButton_2.setText(_translate("MainWindow", "MENU"))
        self.label.setText(_translate("MainWindow", "HI-TECH WEIGHING"))
        self.radioButton_3.setText(_translate("MainWindow", "GROSS"))
        self.radioButton_4.setText(_translate("MainWindow", "TARE"))
        self.lineEdit.setText(_translate("MainWindow", ""))
        self.pushButton_9.setText(_translate("MainWindow", "NEW SLIP"))
        self.pushButton_10.setText(_translate("MainWindow", "OLD SLIP"))
        self.pushButton_6.setText(_translate("MainWindow", "CHECK"))
        self.pushButton_7.setText(_translate("MainWindow", "CLEAR"))
        self.pushButton_11.setText(_translate("MainWindow", "DUPLICATE"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.pushButton_8.setText(_translate("MainWindow", "LOGOUT"))
        
        self.pushButton_8.clicked.connect(MainWindow.close)
        
        self.timer2=QtCore.QTimer()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        connection = sqlite3.connect("fci.db")
        results=connection.execute("SELECT DEVICE_LOCATION_TYPE,IFNULL(OFF_POSITION_SET,0),(IFNULL(CAPACITY_SET,0)*1000),LD_SET FROM GLOBAL_VAR") 
        for x in results:            
            self.device_location_type=str(x[0])
            self.wt_min_limit=int(x[1])
            self.wt_max_limit=int(x[2])
            self.ld_set=int(x[3])
        connection.close()
        
        if(self.device_location_type == "SITE"):
            
            self.pushButton_3.clicked.connect(self.open_new_window6)
            self.pushButton_4.setDisabled(True)
        else:
            
            self.pushButton_3.clicked.connect(self.open_new_window4)
            self.pushButton_4.clicked.connect(self.open_new_window5)
        
        self.pushButton_6.clicked.connect(self.check_onclick)   
        self.pushButton_5.clicked.connect(self.open_new_window7)
        self.pushButton_2.clicked.connect(self.open_new_window8)
        self.pushButton_9.clicked.connect(self.new_field_onlcick)
        self.pushButton_10.clicked.connect(self.old_field_onlcick)
        self.pushButton_7.clicked.connect(self.clear_onclick)
        
        self.pushButton_11.clicked.connect(self.duplicate_onclick)
        self.pushButton.clicked.connect(self.set_zero_fun)
        self.radioButton_3.clicked.connect(self.goss_onclick)
        self.radioButton_4.clicked.connect(self.tare_onclick)
        
        #self.start_wt()
        self.new_slip_hide()
        self.old_slip_hide()
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def goss_onclick(self):
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0, 0, 255);")
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255);")
    
    def tare_onclick(self):
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(0, 0, 255);")
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")

    def clear_onclick(self):
        self.lineEdit.setText("")
        self.label_2.setText("")
    def save_data(self):
        if(self.radioButton_3.isChecked()):
            self.gross_tare_flag="GROSS"
        else:
            self.gross_tare_flag="TARE"
            
        self.old_slip_no=self.lineEdit.text()   
        connection = sqlite3.connect("fci.db")
        with connection:        
            cursor = connection.cursor()
            cursor.execute("UPDATE GLOBAL_VAR SET OLD_NEW_SLIP_FLAG='"+str(self.slip_status)+"' , GROSS_TARE_FLAG='"+str(self.gross_tare_flag)+"' ,OLD_SLIP_NO='"+str(self.old_slip_no)+"', LCD_WEIGHT='"+str(self.current_value)+"'")
        connection.commit();
        connection.close()
        #self.stop_timer()
    
    def start_wt(self):
        #print("Weight Started ....")
        try:
            self.ser = serial.Serial(
                                port='/dev/ttyAMA0',
                                baudrate=115200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.05
                            )
        
            self.ser.flush()       
           
            
            self.line = self.ser.readline(30)
            print("o/p:"+str(self.line))
             
            self.timer2.setInterval(5000)        
            self.timer2.timeout.connect(self.display_lcd_val)
            self.timer2.start(10)
            
            
        except IOError:
            print("IO Errors-load cell connections error")
            self.IO_error_flg=1
            
            
    def display_lcd_val(self):               
        #print(" inside display_lcd_val:"+str(self.IO_error_flg))
        if(self.green_counter > 0):
                self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);")
                self.green_counter=self.green_counter-1
        else:
                self.pushButton.setStyleSheet("background-color: rgb(170, 0, 0);")
        
        if(self.IO_error_flg==0):
            try:
                self.line = self.ser.readline()
                print(" raw o/p:"+str(self.line))
                print("self.line:"+str(self.line,'utf-8'))
                self.xstr0=str(self.line,'utf-8')
                self.xstr1=self.xstr0.replace("\r","")
                self.xstr2=self.xstr1.replace("\n","")
                self.buff=self.xstr2.split("_")
                self.last_value=self.current_value 
                if(len(self.buff)> 1):
                       # if(str(self.buff[3]) == 'R'): 
                                self.xstr2=str(self.buff[0])
                                try:
                                     self.xstr4=int(self.xstr2)
                                except ValueError:                        
                                    print("Value Error"+str(self.xstr2))
                                    self.xstr4=0                    
                                try:
                                    if(int(self.ld_set) > 0):
                                        self.mod_val=0
                                        self.mod_val=(int(self.xstr4) % int(self.ld_set))
                                        self.mod_val=int(self.xstr4)-self.mod_val
                                        self.lcdNumber.setProperty("value", str(self.mod_val))
                                        self.current_value=int(self.mod_val)
                                    else:
                                        self.lcdNumber.setProperty("value", str(self.xstr4))
                                except ValueError:
                                    print("Value Error :"+str(self.xstr4))
                                    self.xstr4=0
                                    self.current_value=0
                                '''
                                if(self.weighing_crosses_min_wt_lim=="Yes" and self.weighing_crosses_max_wt_lim=="No"):    
                                    self.lcdNumber.setProperty("value", str(self.xstr4))                                    
                                else:
                                    self.lcdNumber.setProperty("value", 0)
                                '''
                                if(self.enable_buttons_flag=="Yes"):
                                       self.lcdNumber.setStyleSheet("color: rgb(0, 170, 0);\n background-color: rgb(0, 0, 0);")
                                else:
                                       self.lcdNumber.setStyleSheet("color: rgb(255, 0, 0);\n background-color: rgb(0, 0, 0);")
                                
                                if(float(self.xstr4) > 1100):
                                    self.pushButton.hide()
                                else:
                                    self.pushButton.show()
                                
                                if(self.last_value==self.current_value):
                                        self.enable_counter=self.enable_counter+1
                                        if(self.enable_counter > 15):
                                             self.enable_buttons_flag="Yes"
                                             if(int(self.current_value) > int(self.wt_min_limit)):                                                     
                                                      self.weighing_crosses_min_wt_lim="Yes"
                                             else:
                                                      self.weighing_crosses_min_wt_lim="No"
                                             if(int(self.current_value) > int(self.wt_max_limit)):                                                     
                                                      self.weighing_crosses_max_wt_lim="Yes"
                                             else:
                                                      self.weighing_crosses_max_wt_lim="No"
                                        else:
                                             
                                             self.enable_buttons_flag="No"                                            
                                else:            
                                        self.enable_buttons_flag="No"
                                        self.enable_counter=0
                    
            except IOError:
                print("IO Errors : Data Read Error") 
                self.IO_error_flg=1  
    
    def stop_timer(self):
       if(self.timer2.isActive()):
           self.timer2.stop()
           print("Stoped")
       else:
           print("Already stoped")
           #self.start_wt()
           
    
    def start_timer(self):
        if(self.timer2.isActive()):
           print("Already Started ")
        else:
           print("Started again")
           self.start_wt()
                    
           
    
    def new_slip_hide(self):
        self.radioButton_3.hide()
        self.radioButton_4.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()        
    
    
    def new_slip_show(self):
        self.radioButton_3.show()
        self.radioButton_4.show()
        self.pushButton_3.show()
        self.pushButton_4.show()
        self.pushButton_5.show()
    
    
    
    def display_new_slip_fields(self):
        self.slip_status="NEW"
        if(self.new_slip_flag=="HIDE"):
            self.new_slip_hide()
        elif(self.new_slip_flag=="SHOW"):
            self.new_slip_show()
        else:
            self.new_slip_show()
    
    def new_field_onlcick(self):
        self.start_timer()
        self.old_slip_hide()
        self.new_slip_flag="SHOW"
        self.display_new_slip_fields()
    
    ###########################
    
    def old_slip_hide(self):
        self.pushButton_6.hide()
        self.pushButton_7.hide()
        self.pushButton_11.hide()
        self.label_2.hide()
        self.lineEdit.hide()
    
    
    def old_slip_show(self):
        self.pushButton_6.show()
        self.pushButton_7.show()
        self.pushButton_11.show()
        self.label_2.show()
        self.lineEdit.show()
    
    
    
    def display_old_slip_fields(self):        
        self.slip_status="OLD"
        if(self.old_slip_flag=="HIDE"):
            self.old_slip_hide()
        elif(self.old_slip_flag=="SHOW"):
            self.old_slip_show()
        else:
            self.old_slip_show()
    
    def old_field_onlcick(self):
        self.start_timer()
        self.lineEdit.setFocus(True)
        self.new_slip_hide()
        self.old_slip_flag="SHOW"
        self.display_old_slip_fields()
        
    #####################        
        
    def set_zero_fun(self):
        #self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.green_counter=15
        try:
            self.ser = serial.Serial(
                                port='/dev/ttyAMA0',
                                baudrate=115200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.05
                            )
        
            self.ser.flush() 
       
            self.command_str="T"
            print("Tare Command : "+str(self.command_str))
            b = bytes(self.command_str, 'utf-8')
            self.ser.write(b)
        except IOError:
                print("IO Errors : Data Read Error") 
                self.IO_error_flg=1  
        #time.sleep(2)       
        #self.pushButton.setStyleSheet("background-color: rgb(170, 0, 0);")
        
        
           
    def check_onclick(self):        
        ###Check if serial number exist
        self.save_data()
        self.serial_no = ""
        self.batch_id=""
        self.issue_id=""
        self.dev_loc_type=""
        self.status=""
        self.first_wt_type=""
        if(self.lineEdit.text() != ""):
            connection = sqlite3.connect("fci.db")
            print("SELECT SERIAL_ID ,DEVICE_LOCATION_TYPE,IFNULL(BATCH_ID,0),IFNULL(ISSUE_ID,0),STATUS FROM WEIGHT_MST WHERE SERIAL_ID='"+str(int(self.lineEdit.text()))+"'") 
            
            results=connection.execute("SELECT SERIAL_ID ,DEVICE_LOCATION_TYPE,IFNULL(BATCH_ID,0),IFNULL(ISSUE_ID,0),STATUS,FIRST_WEIGHT_MODE FROM WEIGHT_MST WHERE SERIAL_ID='"+str(int(self.lineEdit.text()))+"'") 
            for x in results:            
                self.serial_no=str(x[0])
                self.batch_id=str(x[2])
                self.issue_id=str(x[3])
                self.dev_loc_type=str(x[1])
                self.status=str(x[4])
                self.first_wt_type=str(x[5])
            connection.close()
            print("first wt mode :"+str(self.first_wt_type))
            connection = sqlite3.connect("fci.db")
            with connection:        
                cursor = connection.cursor()
                cursor.execute("UPDATE GLOBAL_VAR SET OLD_NEW_SLIP_FLAG='OLD' , GROSS_TARE_FLAG='"+str(self.first_wt_type)+"' ,OLD_SLIP_NO='"+str(self.serial_no)+"', LCD_WEIGHT='"+str(self.current_value)+"'")
            connection.commit();
            connection.close()
            
            
            
            if(self.serial_no != ""):
                    if(self.status=="SECOND"):
                        self.label_2.setText("Completed Serial.No :"+str(self.serial_no))
                    else:
                        print("batch_id:"+str(self.batch_id)+" issue_id:"+str(self.issue_id))
                        if(self.batch_id == "" and  self.issue_id==""):
                             self.open_new_window7()
                        else:
                            if(self.batch_id  != ""):
                                 if(int(self.batch_id) > 0):
                                    if(self.dev_loc_type == "STORAGE"):
                                        self.label_2.setText("")
                                        #call recipt of storage
                                        self.open_new_window4()
                                    else:
                                        self.label_2.setText("")
                                        #call recipt of site
                                        self.open_new_window6()
                            elif(self.issue_id  != ""):
                                    if(int(self.issue_id) > 0):
                                            self.label_2.setText("")
                                            #call issue of storage
                                            self.open_new_window5()
                            else:
                                self.label_2.setText("ERROR.")
                                self.label_2.setText("b:"+str(self.batch_id)+" i:"+str(self.issue_id))
            else:
                    self.label_2.setText("SERIAL NO. DOES NOT EXIST.")
        else:
            self.label_2.setText("ENTER SERIAL NO.")
    
    
    def duplicate_onclick(self):        
        ###Check if serial number exist
        self.save_data()
        self.serial_no = ""
        self.batch_id=""
        self.issue_id=""
        self.dev_loc_type=""
        self.status=""
        self.first_wt_type=""
        if(self.lineEdit.text() != ""):
            connection = sqlite3.connect("fci.db")
            results=connection.execute("SELECT SERIAL_ID ,DEVICE_LOCATION_TYPE,IFNULL(BATCH_ID,0),IFNULL(ISSUE_ID,0),STATUS FROM WEIGHT_MST WHERE SERIAL_ID='"+str(int(self.lineEdit.text()))+"'") 
            for x in results:            
                self.serial_no=str(x[0])
                self.batch_id=str(x[2])
                self.issue_id=str(x[3])
                self.dev_loc_type=str(x[1])
                self.status=str(x[4])
            connection.close()
            
            connection = sqlite3.connect("fci.db")
            with connection:        
                cursor = connection.cursor()
                cursor.execute("UPDATE GLOBAL_VAR SET OLD_NEW_SLIP_FLAG='OLD' , GROSS_TARE_FLAG='"+str(self.first_wt_type)+"' ,OLD_SLIP_NO='"+str(self.serial_no)+"', LCD_WEIGHT='"+str(self.current_value)+"'")
            connection.commit();
            connection.close()
            
            
            if(self.serial_no != ""):
                   print("batch_id:"+str(self.batch_id)+" issue_id:"+str(self.issue_id))
                   if(self.batch_id == "" and  self.issue_id==""):
                             self.open_new_window12()
                   else:                       
                       if(self.batch_id  != ""):
                             if(int(self.batch_id) > 0):
                                if(self.dev_loc_type == "STORAGE"):
                                    self.label_2.setText("")
                                    #call recipt of storage
                                    self.open_new_window10()
                                else:
                                    self.label_2.setText("")
                                    #call recipt of site
                                    self.open_new_window11()
                       elif(self.issue_id  != ""):      
                             if(int(self.issue_id) > 0):
                                    self.label_2.setText("")
                                    #call issue of storage
                                    self.open_new_window9()
                             else:
                                self.label_2.setText("ERROR.")
                                self.label_2.setText("b:"+str(self.batch_id)+" i:"+str(self.issue_id))
            else:
                    self.label_2.setText("SERIAL.NO. DOES NOT EXIST.")
        else:
            self.label_2.setText("ENTER SERIAL NO.")
    
    
    def open_new_window4(self):
        if(str(self.slip_status) == "NEW"):
                        self.save_data()
        print("self.slip_status4 :"+str(self.slip_status))
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_03b_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()     
    
    def open_new_window5(self):
        if(str(self.slip_status) == "NEW"):
                        self.save_data()
        print("self.slip_status 5 :"+str(self.slip_status))
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_03i_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window6(self):
        if(str(self.slip_status) == "NEW"):
                self.save_data()
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_03_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window7(self):
        if(str(self.slip_status) == "NEW"):
                self.save_data()
        print("self.slip_status7 :"+str(self.slip_status))
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_34_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window8(self):
        if(str(self.slip_status) == "NEW"):
                self.save_data()
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_01_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    
    #### DUPLICATE PRINT WINDOWS
        
    def open_new_window9(self):
        self.save_data()
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_39_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window10(self):
        self.save_data()
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_40_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window11(self):
        self.save_data()
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_41_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window12(self):
        self.save_data()
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_42_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_04_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
