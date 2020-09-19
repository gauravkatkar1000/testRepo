# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_11_issue_report_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from fci_12_issue_report import fci_12_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem
import datetime
import sqlite3
from PyQt5.QtCore import QDate

class fci_11_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1311, 701))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
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
        self.tableWidget.setGeometry(QtCore.QRect(40, 210, 1241, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 660, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 660, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(430, 20, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(690, 20, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setGeometry(QtCore.QRect(430, 60, 201, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 50, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_33 = QtWidgets.QLabel(self.groupBox_5)
        self.label_33.setGeometry(QtCore.QRect(10, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox_5)
        self.label_34.setGeometry(QtCore.QRect(10, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 70, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 20, 111, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(920, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_7.setEnabled(False)
        self.groupBox_7.setGeometry(QtCore.QRect(920, 50, 191, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 151, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(1160, 80, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 180, 1261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_6.setEnabled(False)
        self.groupBox_6.setGeometry(QtCore.QRect(680, 60, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_11.setGeometry(QtCore.QRect(110, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(910, 650, 361, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.from_date=""
        self.to_date=""
        self.v_param_arr=[]
        self.whr_str=""
        
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(140, 220, 312, 183))
        self.calendarWidget.setGridVisible(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setObjectName("calendarWidget")
        
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget_2.setGeometry(QtCore.QRect(200, 220, 312, 183))
        self.calendarWidget_2.setGridVisible(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calendarWidget_2.setFont(font)
        self.calendarWidget_2.setObjectName("calendarWidget")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00 "))
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
        item.setText(_translate("MainWindow", "Recipt ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "No. Of Trucks."))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Net. Wt."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total.No. Bags"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Release Date"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Release Time"))
        self.pushButton_7.setText(_translate("MainWindow", "Show Report"))
        self.pushButton_8.setText(_translate("MainWindow", "Return"))
        self.radioButton.setText(_translate("MainWindow", "Daily"))
        self.radioButton_2.setText(_translate("MainWindow", "Monthly"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Select Month"))
        self.pushButton_10.setText(_translate("MainWindow", "Date"))
        self.radioButton_3.setText(_translate("MainWindow", "Date Range"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Dates"))
        self.label_33.setText(_translate("MainWindow", "From Date :"))
        self.label_34.setText(_translate("MainWindow", "To  Date :"))
        self.pushButton_5.setText(_translate("MainWindow", "Date"))
        self.pushButton_6.setText(_translate("MainWindow", "Date"))
        self.radioButton_4.setText(_translate("MainWindow", " Order Id only"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Select  Order ID"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ISSUE_20200806_0"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ISSUE_20200805_0"))
        self.pushButton_9.setText(_translate("MainWindow", "Search "))
        self.groupBox_6.setTitle(_translate("MainWindow", "Select Month"))
        self.pushButton_11.setText(_translate("MainWindow", "Month"))
        self.label_21.setText(_translate("MainWindow", "Issues Report as on 07 Aug 2020"))
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.startx()
        
    def startx(self):
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1) 
        self.calendarWidget_2.hide()
        self.calendarWidget.hide()
        self.radioButton.setDisabled(True)
        self.radioButton_2.setDisabled(True)
        
        
    
        
        self.select_all_data()
        self.radioButton_3.clicked.connect(self.date_range_onclick)
        self.radioButton_4.clicked.connect(self.batches_onlick)
        self.pushButton_9.clicked.connect(self.select_all_data)
        self.pushButton_5.clicked.connect(self.DOB_on_click1)
        self.pushButton_6.clicked.connect(self.DOB_on_click2)
        self.pushButton_7.clicked.connect(self.open_new_window2)
        
        self.calendarWidget.clicked.connect(self.calendar1_on_click)
        self.calendarWidget_2.clicked.connect(self.calendar2_on_click)
        
        self.i=0
        connection = sqlite3.connect("fci.db")
        results=connection.execute("SELECT BATCH_ID FROM BATCH_MST ORDER BY BATCH_ID DESC ") 
        for x in results:            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        
        self.lineEdit_2.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.lineEdit_3.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        temp_var =QDate.currentDate()
        var_name = temp_var.toPyDate()
        self.from_date=str(var_name)
        self.to_date=str(var_name)
        self.update_report_param()
        temp_var =QDate.currentDate()
        var_name = temp_var.toPyDate()
        self.from_date=str(var_name)
        self.to_date=str(var_name)      
        self.select_all_data()
        
    
    def date_range_onclick(self):        
        self.groupBox_5.setEnabled(True)  # Datetrange Group
        self.groupBox_7.setDisabled(True)  #Batch oly group         
         
    
    def batches_onlick(self):
        self.groupBox_5.setDisabled(True)  # Datetrange Group
        self.groupBox_7.setEnabled(True)  #Batch oly group  
        
    
    def DOB_on_click1(self):
        self.calendarWidget.show()
    
    def DOB_on_click2(self):
        self.calendarWidget_2.show()
    
    def calendar1_on_click(self):
        temp_var = self.calendarWidget.selectedDate() 
        var_name = temp_var.toPyDate()        
        self.from_date=str(var_name) 
        self.lineEdit_3.setText(str(self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)))
        self.calendarWidget.hide()
    
    def calendar2_on_click(self):
        temp_var = self.calendarWidget_2.selectedDate() 
        var_name = temp_var.toPyDate()        
        self.to_date=str(var_name)
        self.lineEdit_2.setText(str(self.calendarWidget_2.selectedDate().toString(QtCore.Qt.ISODate)))
        self.calendarWidget_2.hide()
    
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def select_all_data(self):
        self.whr_sql=""
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 200)
        self.tableWidget.setColumnWidth(6, 200)    
        self.tableWidget.setColumnWidth(7, 50)
        
        if(self.radioButton_3.isChecked()):
            self.whr_sql=" WHERE strftime('%Y-%m-%d',START_DATE)  between '"+str(self.from_date)+"' and '"+str(self.to_date)+"' limit 400"
        elif(self.radioButton_4.isChecked()):
            self.whr_sql="WHERE ISSUE_ID = '"+self.comboBox.currentText()+"'"
        else:
            self.whr_sql="Order by ISSUE_ID DESC"
      
        self.tableWidget.setHorizontalHeaderLabels(['Order ID.', ' Total Trucks ', 'Total Net.Wt Ton','Total Accpt.Bags.Cnt','Status','Release Date','Release Time' ,'Started On'])        
           
        connection = sqlite3.connect("fci.db")
        print("SELECT (SELECT A.ORDER_ID FROM ISSUE_MST A WHERE A.ISSUE_ID=ISSUE_ID ) as ISSUE_ID,TOTAL_TRUCKS,printf(\"%.3f\", TOTAL_NET_WT),printf(\"%3d\", TOTAL_ACCEPTED_BAGS),STATUS,RELEASE_DATE,RELEASE_TIME,START_DATE FROM ISSUE_LIST_VW "+str(self.whr_sql))                        
       
        results=connection.execute("SELECT (SELECT A.ORDER_ID FROM ISSUE_MST A WHERE A.ISSUE_ID=ISSUE_ID ) as ISSUE_ID,TOTAL_TRUCKS,printf(\"%.3f\", TOTAL_NET_WT),printf(\"%3d\", TOTAL_ACCEPTED_BAGS),STATUS,RELEASE_DATE,RELEASE_TIME,START_DATE FROM ISSUE_LIST_VW "+str(self.whr_sql))                        
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
        self.update_report_param()
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)     
        
        
    def open_new_window2(self):
        self.update_report_param()
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_12_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def update_report_param(self):
        if(self.radioButton_3.isChecked()):
            connection = sqlite3.connect("fci.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET REPORT_ENTITY='ISSUE',REPORT_BY='DATE_RANGE',REPORT_FROM_DATE='"+str(self.from_date)+"',REPORT_TO_DATE='"+str(self.to_date)+"',REPORT_BATCH_ID=null")
            
            connection.commit();                    
            connection.close() 
        elif(self.radioButton_4.isChecked()):
            connection = sqlite3.connect("fci.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET REPORT_ENTITY='ISSUE',REPORT_BY='BY_ISSUE_ID',REPORT_FROM_DATE=null,REPORT_TO_DATE=null,REPORT_ISSUE_ID='"+self.comboBox.currentText()+"'")
            
         
            
            connection.commit();                    
            connection.close()
        else:
            print("none")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_11_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
