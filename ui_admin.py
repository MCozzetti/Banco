# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created: Thu Sep  2 11:29:23 2021
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class admin_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1123, 749)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.text_consulta = QtGui.QTextEdit(self.centralwidget)
        self.text_consulta.setGeometry(QtCore.QRect(30, 20, 731, 31))
        self.text_consulta.setObjectName(_fromUtf8("text_consulta"))
        self.btn_ejecutar = QtGui.QPushButton(self.centralwidget)
        self.btn_ejecutar.setGeometry(QtCore.QRect(780, 20, 90, 27))
        self.btn_ejecutar.setObjectName(_fromUtf8("btn_ejecutar"))
        self.btn_borrar = QtGui.QPushButton(self.centralwidget)
        self.btn_borrar.setGeometry(QtCore.QRect(890, 20, 90, 27))
        self.btn_borrar.setObjectName(_fromUtf8("btn_borrar"))
        self.btn_salir = QtGui.QPushButton(self.centralwidget)
        self.btn_salir.setGeometry(QtCore.QRect(1000, 20, 90, 27))
        self.btn_salir.setObjectName(_fromUtf8("btn_salir"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 1071, 331))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lista_tablas = QtGui.QListWidget(self.centralwidget)
        self.lista_tablas.setGeometry(QtCore.QRect(30, 480, 431, 192))
        self.lista_tablas.setObjectName(_fromUtf8("lista_tablas"))
        self.lista_atributos = QtGui.QListWidget(self.centralwidget)
        self.lista_atributos.setGeometry(QtCore.QRect(660, 480, 431, 192))
        self.lista_atributos.setObjectName(_fromUtf8("lista_atributos"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 450, 151, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 450, 131, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_ejecutar.setText(_translate("MainWindow", "Ejecutar", None))
        self.btn_borrar.setText(_translate("MainWindow", "Borrar", None))
        self.btn_salir.setText(_translate("MainWindow", "Salir", None))
        self.label.setText(_translate("MainWindow", "Lista de Tablas", None))
        self.label_2.setText(_translate("MainWindow", "Lista de Atributos", None))

