# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'TY_06_REPORT_PART_2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem

import sqlite3

class TY_06_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 1331, 651))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.frame.setObjectName("frame")
        
        self.shape=""       
        self.unit_typex=""
        self.lastIndex=13
        
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(540, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        
        self.label_6_1 = QtWidgets.QLabel(self.frame)
        self.label_6_1.setGeometry(QtCore.QRect(840, 30, 351, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_6_1.setFont(font)
        #self.label_6.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_6_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6_1.setObjectName("label_6_1")
        
        
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(570, 600, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setGeometry(QtCore.QRect(20, 111, 1291, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        '''
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(670, 110, 641, 411))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        '''
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.test_type=""
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Report Part II")) 
        self.label_6_1.setText(_translate("MainWindow", " [ Test Id: 265 ]    [ Batch Id : 3452321qwe ] "))
        self.pushButton_14.setText(_translate("MainWindow", "Return"))
        self.pushButton_14.clicked.connect(MainWindow.close)
        
        #self.select_all_rows_2()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TEST_ID,BATCH_ID,TEST_TYPE FROM TEST_MST WHERE TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)") 
        for x in results:           
            self.label_6_1.setText("[ Test Id: "+str(x[0])+" ]              [ Batch Id:"+str(x[1])+" ]")
            self.test_type=str(x[2])
        connection.close()
        
        if(self.test_type=="Compress"):
            self.select_all_rows_compress()
        elif(self.test_type=="Tear"):
            self.select_all_rows_tear()
        elif(self.test_type=="Flexural"):
            self.select_all_rows_flexural()
        else:
            self.select_all_rows()
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)       
            
    def select_all_rows(self):
        self.delete_all_records()    
        self.tableWidget.setMidLineWidth(-4)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView { font-size:  10pt};")
        self.tableWidget.verticalHeader().setStyleSheet("QHeaderView { font-size:  10pt};")
        #self.tableWidget.horizontalHeader().setStyleSheet("::section {background-color : lightGray;font-size:10pt;}")
   
        #self.tableWidget.setRowCount(1)
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 80)
        self.tableWidget.setColumnWidth(4, 120)
        self.tableWidget.setColumnWidth(5, 80)
        self.tableWidget.setColumnWidth(6, 80)    
        self.tableWidget.setColumnWidth(7, 120)
        self.tableWidget.setColumnWidth(8, 80)    
        self.tableWidget.setColumnWidth(9, 120)
        self.tableWidget.setColumnWidth(10, 100)
        self.tableWidget.setColumnWidth(11, 100)
        self.tableWidget.setColumnWidth(12, 100)    
        self.tableWidget.setColumnWidth(13, 100)
        
     
        
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
        for x in results:           
            self.unit_typex=x[1]
        connection.close()
        
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
           
        # SELECT SHAPE FROM SPECIMEN_MST WHERE SPECIMEN_NAME IN ( SELECT SPECIMEN_NAME FROM TEST_MST WHERE TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SHAPE FROM SPECIMEN_MST WHERE SPECIMEN_NAME IN ( SELECT SPECIMEN_NAME FROM TEST_MST WHERE TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR))") 
        for x in results:
            self.shape=x[0]
        connection.close()
        #self.shape='Pipe'                                 
        print ("shape :"+self.shape)        
        if (self.shape=="Rectangle"):
            if(self.unit_typex=="Lb/Inch"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe.No.', ' Thickness \n (Inch) ', ' Width \n (Inch) ', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak','E@Break \n (Inch)','% E@Break','Tensile Strength \n (Lb/Inch2)','Mod@100% \n (Lb/Inch2)','Mod@200% \n (Lb/Inch2)','Mod@300% \n (Lb/Inch2)','Mod % (Lb/Inch2)' ])        
            elif(self.unit_typex == "Newton/Mm"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe.No.', ' Thickness \n (mm) ', ' Width \n (mm) ', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (N/Mm2)','Mod@100% \n (N/Mm2)','Mod@200% \n (N/Mm2)','Mod@300% \n (N/Mm2)','Mod %'])
            elif(self.unit_typex == "MPA"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe.No.', ' Thickness \n (mm) ', ' Width \n (mm) ', 'CS.Area \n (mm2)','Force at Peak \n (Kg)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (MPA)','Mod@100% \n (MPA)','Mod@200% \n (MPA)','Mod@300% \n (MPA)','Mod %'])
            else:    
                self.tableWidget.setHorizontalHeaderLabels(['Spe.No.', ' Thickness \n (cm) ', ' Width \n (cm) ', 'CS.Area \n (cm2)','Force at Peak \n (Kg)' ,'E@Peak \n (cm)','% E@Peak','E@Break \n (cm)','% E@Break','Tensile Strength \n (Kg/Cm2)','Mod@100% \n (Kg/Cm2)','Mod@200% \n (Kg/Cm2)','Mod@300% \n (Kg/Cm2)','Mod %'])        
        elif (self.shape=="Cylindrical"):     
            self.tableWidget.setColumnCount(13)
            self.lastIndex=12
            if(self.unit_typex=="Lb/Inch"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Diameter \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak','E@Break \n (Inch)','% E@Break','Tensile Strength \n (Lb/Inch2)','Mod@100% \n (Lb/Inch2)','Mod@200% \n (Lb/Inch2)','Mod@300% \n (Lb/Inch2)','Mod % (Lb/Inch2)'])
            elif(self.unit_typex == "Newton/Mm"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Diameter \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (N/Mm2)','Mod@100% \n (N/Mm2)','Mod@200% \n (N/Mm2)','Mod@300% \n (N/Mm2)','Mod %'])
            elif(self.unit_typex == "MPA"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Diameter \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (Kg)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (MPA)','Mod@100% \n (MPA)','Mod@200% \n (MPA)','Mod@300% \n (MPA)','Mod %'])
            else: 
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Diameter \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (Kg)' ,'E@Peak \n (cm)','% E@Peak','E@Break \n (cm)','% E@Break','Tensile Strength \n (Kg/Cm2)','Mod@100% \n (Kg/Cm2)','Mod@200% \n (Kg/Cm2)','Mod@300% \n (Kg/Cm2)','Mod %'])
        
        elif (self.shape=="Pipe"):            
            self.tableWidget.setColumnCount(14)
            self.lastIndex=13
            if(self.unit_typex=="Lb/Inch"):
               self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Inn.Diameter \n (Inch)', 'Out. Diameter \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak','E@Break \n (Inch)','% E@Break','Tensile Strength \n (Lb/Inch2)','Mod@100% \n (Lb/Inch2)','Mod@200% \n (Lb/Inch2)','Mod@300% \n (Lb/Inch2)','Mod % (Lb/Inch2)'])
            elif(self.unit_typex == "Newton/Mm"):
               self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Inn.Diameter \n (Inch)', 'Out. Diameter \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (N/Mm2)','Mod@100% \n (N/Mm2)','Mod@200% \n (N/Mm2)','Mod@300% \n (N/Mm2)','Mod %']) 
            elif(self.unit_typex == "MPA"):
               self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Inn.Diameter \n (mm)', 'Out. Diameter \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (Kg)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (MPA)','Mod@100% \n (MPA)','Mod@200% \n (MPA)','Mod@300% \n (MPA)','Mod %']) 
            else:
               self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Inn.Diameter \n (cm)', 'Out. Diameter \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (Kg)' ,'E@Peak \n (cm)','% E@Peak','E@Break \n (cm)','% E@Break','Tensile Strength \n (Kg/Cm2)','Mod@100% \n (Kg/Cm2)','Mod@200% \n (Kg/Cm2)','Mod@300% \n (Kg/Cm2)','Mod %'])
        elif (self.shape=="DirectValue"): 
            self.tableWidget.setColumnCount(12)
            self.lastIndex=11
            if(self.unit_typex=="Lb/Inch"):
                #print("header")
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak','E@Break \n (Inch)','% E@Break','Tensile Strength \n (Lb/Inch2)','Mod@100% \n (Lb/Inch2)','Mod@200% \n (Lb/Inch2)','Mod@300% \n (Lb/Inch2)','Mod %'])           
            elif(self.unit_typex == "Newton/Mm"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'CS.Area \n (mm2)','Force at Peak \n (Kg)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (N/Mm2)','Mod@100% \n (N/Mm2)','Mod@200% \n (N/Mm2)','Mod@300% \n (N/Mm2)','Mod %'])
            elif(self.unit_typex == "MPA"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'CS.Area \n (mm2)','Force at Peak \n (Kg)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (MPA)','Mod@100% \n (MPA)','Mod@200% \n (MPA)','Mod@300% \n (MPA)','Mod %'])
            else:   
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'CS.Area \n (cm2)','Force at Peak \n (Kg)' ,'E@Peak \n (cm)','% E@Peak','E@Break \n (cm)','% E@Break','Tensile Strength \n (Kg/Cm2)','Mod@100% \n (Kg/Cm2)','Mod@200% \n (Kg/Cm2)','Mod@300% \n (Kg/Cm2)','Mod %'])           
        else:
           self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Thickness \n (mm)', 'Width \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (kg)' ,'% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (Kg/Cm2)','Mod@100% \n (Kg/Cm2)','Mod@200% \n (Kg/Cm2)','Mod@300% \n (Kg/Cm2)','Mod %'])
       
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT MOD_AT_ANY FROM REPORT_MST WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                        
        for rows in results:
                print(" self.lastIndex :"+str(self.lastIndex))
                item = self.tableWidget.horizontalHeaderItem(self.lastIndex)
                if(self.unit_typex=="Lb/Inch"):
                    item.setText("Mod@"+str(rows[0])+"% \n (Lb/Inch2)")
                elif(self.unit_typex == "Newton/Mm"):
                    item.setText("Mod@"+str(rows[0])+"% \n (N/Mm2)")                    
                elif(self.unit_typex == "MPA"):
                    item.setText("Mod@"+str(rows[0])+"% \n (MPA)")    
                else: 
                    item.setText("Mod@"+str(rows[0])+"% \n (Kg/Cm2)")   
             
        connection = sqlite3.connect("tyr.db")
        print("shape : "+str(self.shape))
        if (self.shape=="Rectangle"):            
            results=connection.execute("SELECT TYPE_STR as specimen_no,round(THICKNESS,2),round(WIDTH,2),round(CS_AREA,2),round(PEAK_LOAD,2),round(E_PAEK_LOAD,2),round(PREC_E_AT_PEAK,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2)  FROM REPORT_PART_2_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
            results1=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,round(A.THICKNESS,2),round(A.WIDTH,2),round(A.CS_AREA,2),round(A.PEAK_LOAD,2),round(A.E_PAEK_LOAD,2),round(PREC_E_AT_PEAK,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID,round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2 WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")       
        elif (self.shape=="Cylindrical"):
            results=connection.execute("SELECT TYPE_STR as specimen_no,round(DIAMETER,2),round(CS_AREA,2),round(PEAK_LOAD,2),round(E_PAEK_LOAD,2),round(PREC_E_AT_PEAK,2),round(BREAK_LOAD,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
            results1=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,round(A.DIAMETER,2),round(A.CS_AREA,2),round(A.PEAK_LOAD,2),round(A.E_PAEK_LOAD,2),round(PREC_E_AT_PEAK,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_PART_2 WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")
        elif (self.shape=="Pipe"):
            results=connection.execute("SELECT TYPE_STR as specimen_no,round(INN_DIAMETER,2),round(OUT_DIAMTER,2),round(CS_AREA,0),round(PEAK_LOAD,2),round(E_PAEK_LOAD,2) ,round(PREC_E_AT_PEAK,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")           
            results1=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,round(A.INN_DIAMETER,2),round(A.OUT_DIAMTER,2),round(A.CS_AREA,2),round(A.PEAK_LOAD,2),round(A.E_PAEK_LOAD,2),round(PREC_E_AT_PEAK,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_PART_2 WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")       
        elif (self.shape=="DirectValue"):
            #print("CD values ")
            #print("SELECT TYPE_STR as specimen_no,round(CS_AREA,0),round(PEAK_LOAD,2),round(E_PAEK_LOAD,2),round(PREC_E_AT_PEAK,2),round(BREAK_LOAD,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
        
            #print("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,round(A.CS_AREA,2),A.PEAK_LOAD,A.E_PAEK_LOAD,round(PREC_E_AT_PEAK,2),round(BREAK_LOAD,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_PART_2 WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")        
           

            results=connection.execute("SELECT TYPE_STR as specimen_no,round(CS_AREA,0),round(PEAK_LOAD,2),round(E_PAEK_LOAD,2),round(PREC_E_AT_PEAK,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
            results1=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,round(A.CS_AREA,2),round(A.PEAK_LOAD,2),round(A.E_PAEK_LOAD,2),round(PREC_E_AT_PEAK,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_PART_2 WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")           
        else:
            results=connection.execute("SELECT TYPE_STR as specimen_no,round(THICKNESS,2),round(WIDTH,2),round(CS_AREA,2),round(PEAK_LOAD,2),E_PAEK_LOAD,PERCENTG_E_PEAK_LOAD_MM,PERCENTG_E_PEAK_LOAD,round(PREC_E_AT_PEAK,2),round(BREAK_LOAD,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
            results1=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,round(A.THICKNESS),round(A.WIDTH,2),round(A.CS_AREA,2),round(A.PEAK_LOAD,2),A.E_PAEK_LOAD,A.PERCENTG_E_PEAK_LOAD_MM,A.PERCENTG_E_PEAK_LOAD,round(PREC_E_AT_PEAK,2),round(BREAK_LOAD,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2),round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2),round(MOD_AT_ANY,2) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_PART_2 WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")
                
        #results=connection.execute("SELECT TYPE_STR as specimen_no,THICKNESS,WIDTH,CS_AREA,PEAK_LOAD,E_PAEK_LOAD,PERCENTG_E_PEAK_LOAD_MM,PERCENTG_E_PEAK_LOAD FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                        
        for row_number, row_data in enumerate(results):                        
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                
        #results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,A.THICKNESS,A.WIDTH,A.CS_AREA,A.PEAK_LOAD,A.E_PAEK_LOAD,A.PERCENTG_E_PEAK_LOAD_MM,A.PERCENTG_E_PEAK_LOAD FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")                        
        for row_number, row_data in enumerate(results1):                    
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):                
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                
                                        
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)     
        connection.close()    

    def select_all_rows_compress(self):
        self.delete_all_records()    
        self.tableWidget.setMidLineWidth(-4)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView { font-size:  10pt};")
        self.tableWidget.verticalHeader().setStyleSheet("QHeaderView { font-size:  10pt};")
        
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 180)
        self.tableWidget.setColumnWidth(4, 280)
        self.tableWidget.setColumnWidth(5, 50)
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
        for x in results:           
            self.unit_typex=x[1]
        connection.close()
        
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
           
        if(self.unit_typex == "Kg/Cm"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No', 'CS Area \n (cm2)', 'Force at Peak\n (Kg)', 'Compression \n (cm)', 'Compressive Strength \n (Kg/Cm2)','% Compression \n'])
        elif(self.unit_typex == "Lb/Inch"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No', 'CS Area \n (Inch2)', 'Force at Peak\n (Lb)', 'Compression \n (Inch)', 'Compressive Strength \n (Lb/Inch2)','% Compression \n'])           
        elif(self.unit_typex == "Newton/Mm"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No', 'CS Area \n (mm2)', 'Force at Peak\n (N)', 'Compression \n (mm)', 'Compressive Strength \n (N/mm2)','% Compression \n'])            
        elif(self.unit_typex == "MPA"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No', 'CS Area \n (mm2)', 'Force at Peak\n (MPA)', 'Compression \n (mm)', 'Compressive Strength \n (MPA)','% Compression \n'])           
        else:
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No', 'CS Area \n (mm2)', 'Force at Peak\n (MPA)', 'Compression \n (mm)', 'Compressive Strength \n (MPA)','% Compression \n'])
          
        
       
        connection = sqlite3.connect("tyr.db")
        results1=connection.execute("SELECT TYPE_STR,round(CS_AREA,2),round(PEAK_LOAD,2),round(E_PAEK_LOAD,2),round(COMPRESSIVE_STRENGTH,2),round(PREC_E_AT_BREAK,0) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
            
        #results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,A.THICKNESS,A.WIDTH,A.CS_AREA,A.PEAK_LOAD,A.E_PAEK_LOAD,A.PERCENTG_E_PEAK_LOAD_MM,A.PERCENTG_E_PEAK_LOAD FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")                        
        for row_number, row_data in enumerate(results1):                    
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):                
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                
        connection.close()                                    
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,round(A.CS_AREA,2),round(A.PEAK_LOAD,2),round(A.E_PAEK_LOAD,2),round(A.COMPRESSIVE_STRENGTH,2),round(A.PREC_E_AT_BREAK,0) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        for row_number, row_data in enumerate(results):                    
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        connection.close()
        
        
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)     
    
    def select_all_rows_tear(self):
        self.delete_all_records()    
        self.tableWidget.setMidLineWidth(-4)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView { font-size:  10pt};")
        self.tableWidget.verticalHeader().setStyleSheet("QHeaderView { font-size:  10pt};")
        
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 120)
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
        for x in results:           
            self.unit_typex=x[1]
        connection.close()
        
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
           
        if(self.unit_typex == "Kg/Cm"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No', 'Thickness \n (cm)', 'Force at Peak\n (Kg)', 'Tear Strength \n (Kg/Cm)'])
        elif(self.unit_typex == "Lb/Inch"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No', 'Thickness \n (Inch)', 'Force at Peak\n (Lb)', 'Tear Strength \n (Lb/Inch)'])           
        elif(self.unit_typex == "Newton/Mm"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No', 'Thickness\n (mm)', 'Force at Peak\n (N)', 'Tear Strength \n (N/mm)'])            
        elif(self.unit_typex == "MPA"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No', 'Thickness\n (mm)', 'Force at Peak\n (MPA)', 'Tear Strength \n (MPA)'])           
        else:
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No', 'Thickness \n (mm)', 'Force at Peak\n (MPA)', 'Tear Strength \n (MPA)'])
          
        
       
        connection = sqlite3.connect("tyr.db")
        results1=connection.execute("SELECT TYPE_STR,round(THICKNESS,2),round(PEAK_LOAD,2),round(E_PAEK_LOAD,2),round(TEAR_STRENGTH ,2)  FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
            
        #results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,A.THICKNESS,A.WIDTH,A.CS_AREA,A.PEAK_LOAD,A.E_PAEK_LOAD,A.PERCENTG_E_PEAK_LOAD_MM,A.PERCENTG_E_PEAK_LOAD FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")                        
        for row_number, row_data in enumerate(results1):                    
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):                
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                
        connection.close()                                    
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,round(A.THICKNESS,2),round(A.PEAK_LOAD,2),round(A.TEAR_STRENGTH ,2)  FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        for row_number, row_data in enumerate(results):                    
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        connection.close()
        
        
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  
   
   
    def select_all_rows_flexural(self):
        self.delete_all_records()    
        self.tableWidget.setMidLineWidth(-4)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView { font-size:  10pt};")
        self.tableWidget.verticalHeader().setStyleSheet("QHeaderView { font-size:  10pt};")
        
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 120)
        self.tableWidget.setColumnWidth(4, 180)
        self.tableWidget.setColumnWidth(5, 180)
        self.tableWidget.setColumnWidth(6, 50)
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
        for x in results:           
            self.unit_typex=x[1]
        connection.close()
        
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
           
        if(self.unit_typex == "Kg/Cm"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No','Thickness  \n (cm)','Width  \n (cm)','Span  \n (cm)', 'Length at Peak \n (cm)', 'Force at Peak\n (Kg)', 'Flexural Strength \n (Kg/cm2) '])
        elif(self.unit_typex == "Lb/Inch"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No','Thickness  \n (Inch)','Width  \n (Inch)','Span  \n (Inch)', 'Length at Peak \n (Inch)', 'Force at Peak\n (Lb)', 'Flexural Strength \n (Lb/Inch2)  '])           
        elif(self.unit_typex == "Newton/Mm"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No','Thickness  \n (mm)','Width  \n (mm)','Span  \n (mm)', 'Length at Peak \n (mm)', 'Force at Peak\n (N)', 'Flexural Strength \n (N/mm2)'])            
        elif(self.unit_typex == "MPA"):
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No','Thickness  \n (mm)','Width  \n (mm)','Span  \n (mm)', 'Length at Peak \n (mm)', 'Force at Peak\n (Kg)', 'Flexural Strength \n (MPA)'])           
        else:
            self.tableWidget.setHorizontalHeaderLabels(['Spec. \n No', 'Thickness  \n (mm)','Width  \n (mm)','Span  \n (mm)','Length at Peak \n (mm)', 'Force at Peak\n (Kg)', 'Flexural Strength \n (MPA)'])
          
        
       
        connection = sqlite3.connect("tyr.db")
        results1=connection.execute("SELECT TYPE_STR,round(THICKNESS,2),round(WIDTH,2),round(SPAN,2),round(E_PAEK_LOAD,2),round(PEAK_LOAD,2),round(FLEXURAL_STRENGTH ,2)  FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
            
        #results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,A.THICKNESS,A.WIDTH,A.CS_AREA,A.PEAK_LOAD,A.E_PAEK_LOAD,A.PERCENTG_E_PEAK_LOAD_MM,A.PERCENTG_E_PEAK_LOAD FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")                        
        for row_number, row_data in enumerate(results1):                    
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):                
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                
        connection.close()                                    
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,round(A.THICKNESS,2),round(A.WIDTH,2),round(A.SPAN,2),round(A.E_PAEK_LOAD,2),round(A.PEAK_LOAD,0),round(A.FLEXURAL_STRENGTH ,2)   FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        for row_number, row_data in enumerate(results):                    
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        connection.close()
        
        
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  
   
   
   
   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_06_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())