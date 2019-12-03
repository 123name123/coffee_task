# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 60, 1001, 501))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(10, 0, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.load.setFont(font)
        self.load.setObjectName("load")
        self.red = QtWidgets.QPushButton(self.centralwidget)
        self.red.setGeometry(QtCore.QRect(510, 0, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.red.setFont(font)
        self.red.setObjectName("red")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 26))
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
        self.load.setText(_translate("MainWindow", "Загрузить\\обновить базу"))
        self.red.setText(_translate("MainWindow", "Редактировать базу"))
