# encoding: utf-8
import sys
from PyQt4 import QtCore, QtGui, uic
import mysql.connector as mc
from ui_login import *
from ui_admin import *
import Admin

        
class MainWindow(QtGui.QMainWindow, Login):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_ingresar.clicked.connect(self.Login)
        self.dialog = Admin.a_MainWindow(self)
        self.centerOnScreen()

    def centerOnScreen (self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())        

    def Login(self):
        usuario = self.log_user.text()
        contrasenia = self.log_pass.text()
        mydb = mc.connect(
            host="localhost",
            user= "root",
            password= "",
            database="BANCO"
            )

        if (usuario == "admin" and contrasenia == "admin"):
            self.lbl_res.setText("SAPEE")
            self.dialog.show()
            self.hide()

  

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Main = MainWindow(None)
    Main.show()
    sys.exit(app.exec_())  

    