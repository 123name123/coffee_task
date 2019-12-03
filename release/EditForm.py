# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1033, 641)
        self.add = QtWidgets.QPushButton(Form)
        self.add.setGeometry(QtCore.QRect(10, 10, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(10, 70, 1001, 501))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.delet = QtWidgets.QPushButton(Form)
        self.delet.setGeometry(QtCore.QRect(510, 10, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.delet.setFont(font)
        self.delet.setObjectName("delet")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(270, 580, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.save.setFont(font)
        self.save.setObjectName("save")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add.setText(_translate("Form", "Добавить запись"))
        self.delet.setText(_translate("Form", "Удалить запись"))
        self.save.setText(_translate("Form", "Сохранить"))
