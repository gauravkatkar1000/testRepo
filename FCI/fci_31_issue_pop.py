# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_31_issue_pop.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 384)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 731, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget.setGeometry(QtCore.QRect(20, 80, 681, 221))
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(5, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(6, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(7, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_0.setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_0.setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_0.setFont(3, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_0.setFont(4, font)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        item_0.setFont(5, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_0.setFont(7, font)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(570, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(260, 10, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 21))
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
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Issue_ID"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Issue.Order.Id."))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Vehicle_ ID"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "No.Of.Bags"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Net.Wt.Tone"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "Slip.No."))
        self.treeWidget.headerItem().setText(6, _translate("MainWindow", "Batch Id."))
        self.treeWidget.headerItem().setText(7, _translate("MainWindow", "Dispatched On"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "R0001"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "xxxxxerexx"))
        self.treeWidget.topLevelItem(0).setText(2, _translate("MainWindow", "fdgdfgdfgfd"))
        self.treeWidget.topLevelItem(0).setText(3, _translate("MainWindow", "fdgfdgfdg"))
        self.treeWidget.topLevelItem(0).setText(4, _translate("MainWindow", "fdgdfgfdg"))
        self.treeWidget.topLevelItem(0).setText(5, _translate("MainWindow", "dfgfdgf"))
        self.treeWidget.topLevelItem(0).setText(7, _translate("MainWindow", "fdgfdg"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_9.setText(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", "Issue Details"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())