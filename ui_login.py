# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Mon Aug 30 12:49:05 2021
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

class Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(346, 266)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_ingresar = QtGui.QPushButton(self.centralwidget)
        self.btn_ingresar.setGeometry(QtCore.QRect(130, 160, 90, 27))
        self.btn_ingresar.setObjectName(_fromUtf8("btn_ingresar"))
        self.log_user = QtGui.QLineEdit(self.centralwidget)
        self.log_user.setGeometry(QtCore.QRect(170, 60, 113, 23))
        self.log_user.setObjectName(_fromUtf8("log_user"))
        self.log_pass = QtGui.QLineEdit(self.centralwidget)
        self.log_pass.setGeometry(QtCore.QRect(170, 110, 113, 23))
        self.log_pass.setObjectName(_fromUtf8("log_pass"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 60, 67, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lbl_res = QtGui.QLabel(self.centralwidget)
        self.lbl_res.setGeometry(QtCore.QRect(96, 200, 171, 20))
        self.lbl_res.setText(_fromUtf8(""))
        self.lbl_res.setObjectName(_fromUtf8("lbl_res"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 346, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_ingresar.setText(_translate("MainWindow", "Ingresar", None))
        self.label.setText(_translate("MainWindow", "Usuario", None))
        self.label_2.setText(_translate("MainWindow", "Contraseña", None))

