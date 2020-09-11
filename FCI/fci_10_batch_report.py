# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_10_batch_report.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.Qt import QTableWidgetItem
import datetime
import sqlite3
from PyQt5.QtCore import QDate
import os,sys

class fci_10_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1311, 701))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 85, 127);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(1140, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 190, 1261, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
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
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(20, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(280, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 650, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 650, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(410, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 650, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(500, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(610, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(270, 70, 551, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("")
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(20, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(140, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.login_user_id=""
        self.login_user_role=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Batch Report as on "+datetime.datetime.now().strftime("%d %b %Y")))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45 :00"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Batch Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Truck Sr. No"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Truck RTO No."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Relese date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "No. Bags"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Net. Wt."))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Tare Wt. Ton"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Gross Wt. Ton"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Target Location"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Target Slot.No"))
        self.label_22.setText(_translate("MainWindow", "Report Type :"))
        self.label_2.setText(_translate("MainWindow", "Monthly"))
        self.label_29.setText(_translate("MainWindow", "Net. Weight(Ton) :"))
        self.pushButton_5.setText(_translate("MainWindow", "Refersh"))
        self.pushButton_7.setText(_translate("MainWindow", "Print  Report"))
        self.label_8.setText(_translate("MainWindow", "5450"))
        self.pushButton_8.setText(_translate("MainWindow", "Retrun"))
        self.label_30.setText(_translate("MainWindow", "Total Trucks :"))
        self.label_11.setText(_translate("MainWindow", "150"))
        self.label_36.setText(_translate("MainWindow", "Report selected Month : MAY 2020"))
        self.label_23.setText(_translate("MainWindow", "No. Of Batches :"))
        self.label_9.setText(_translate("MainWindow", "5450"))
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.startx()
    
    def startx(self):
        self.whr_sql=""
        self.whr_sql2=""
        self.pushButton_5.clicked.connect(self.select_all_data)
        self.pushButton_7.clicked.connect(self.print_report)
        connection = sqlite3.connect("fci.db")
        results=connection.execute("SELECT LOGIN_USER_ID ,LOGIN_USER_ROLE FROM GLOBAL_VAR") 
        for x in results:
            self.login_user_id=str(x[0])
            self.login_user_role=str(x[1])
        connection.close()
        #print("self.login_user_role :"+str(self.login_user_role))
        
        connection = sqlite3.connect("fci.db")
        results=connection.execute("SELECT REPORT_ENTITY,REPORT_BY,REPORT_FROM_DATE,REPORT_TO_DATE,REPORT_BATCH_ID  FROM GLOBAL_VAR") 
        for x in results:            
                 self.label_2.setText(str(x[1]))
                 if(self.label_2.text() == 'DATE_RANGE'):
                     self.label_36.setText("Report selected for date range "+str(x[2])+" to "+str(x[3])+".")
                     
                     self.whr_sql=" WHERE strftime('%Y-%m-%d',START_DATE)  between '"+str(x[2])+"' and '"+str(x[3])+"' limit 400"
                     self.whr_sql2=" WHERE strftime('%Y-%m-%d',IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON))  between '"+str(x[2])+"' and '"+str(x[3])+"' order by batch_id,CURR_TRUCK_CNT limit 400"
                 elif(self.label_2.text() == 'BY_BATCH_ID'):
                     self.label_36.setText("Report selected for batch id:"+str(x[4])+".")
                     
                     self.whr_sql="WHERE BATCH_ID = '"+str(x[4])+"'"
                     self.whr_sql2="WHERE BATCH_ID = '"+str(x[4])+"' order by batch_id,CURR_TRUCK_CNT "
                     
                 else:
                     self.label_36.setText("Report selected for unknow.")
        connection.close()
        
        connection = sqlite3.connect("fci.db")
        #print("select count(BATCH_ID),sum(TOTAL_TRUCKS),SUM(TOTAL_NET_WT) from BATCH_LIST_VW "+str(self.whr_sql))
        results=connection.execute("select count(BATCH_ID),sum(TOTAL_TRUCKS),round(SUM(TOTAL_NET_WT),3) from BATCH_LIST_VW "+str(self.whr_sql)) 
        for x in results:            
                     self.label_9.setText(str(x[0]))
                     self.label_11.setText(str(x[1]))
                     self.label_8.setText(str(x[2]))
        connection.close()
        
        self.select_all_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1) 
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def print_report(self):        
         os.system("./job_print_report.sh")
                        
    def select_all_data(self):
        
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 100)    
        self.tableWidget.setColumnWidth(7, 100)
        self.tableWidget.setColumnWidth(8, 150)
        self.tableWidget.setColumnWidth(9, 200)    
        self.tableWidget.setColumnWidth(10, 100)
        
        
        
        print("whr_sql2 :"+str(self.whr_sql2))
        self.tableWidget.setHorizontalHeaderLabels(['Batch ID.', ' Truck Sr. No ', 'Vehical No.','No. Bags','Release Date','Release Time' ,'Net. Wt.Ton','Tare Wt.Ton','Gross Wt.Ton','Target Location'])        
           
        connection = sqlite3.connect("fci.db")
        if(self.login_user_role in ['SUPER_ADMIN','ADMIN','SUPERVISOR']):
                results=connection.execute("SELECT printf(\"%06d\", BATCH_ID) as BATCH_ID,CURR_TRUCK_CNT||MANNUAL_INS_FLG,VEHICLE_NO,printf(\"%3d\", ACCPTED_BAGS) ,SUBSTR(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON),1,11) AS RELEASE_DATE,SUBSTR(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON),11,6) AS RELEASE_TIME,printf(\"%.3f\", NET_WEIGHT_VAL) as NET_WEIGHT_VAL,printf(\"%.3f\", TARE_WT_VAL) as TARE_WT_VAL,printf(\"%.3f\", GROSS_WT_VAL) as GROSS_WT_VAL,TARGET_STORAGE FROM WEIGHT_MST_FCI_VW "+str(self.whr_sql2))                        
      
        else:
                results=connection.execute("SELECT printf(\"%06d\", BATCH_ID) as BATCH_ID,CURR_TRUCK_CNT,VEHICLE_NO,printf(\"%3d\", ACCPTED_BAGS) ,SUBSTR(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON),1,11) AS RELEASE_DATE,SUBSTR(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON),11,6) AS RELEASE_TIME,printf(\"%.3f\", NET_WEIGHT_VAL) as NET_WEIGHT_VAL,printf(\"%.3f\", TARE_WT_VAL) as TARE_WT_VAL,printf(\"%.3f\", GROSS_WT_VAL) as GROSS_WT_VAL,TARGET_STORAGE FROM WEIGHT_MST_FCI_VW "+str(self.whr_sql2))                        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                #self.lineEdit.setText("")
        connection.close()   
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)     
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_10_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
