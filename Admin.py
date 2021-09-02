# encoding: utf-8
import sys
from PyQt4.QtSql import QSqlDatabase, QSqlQuery
from PyQt4.QtCore import QStringList, QString
from PyQt4.QtGui import (QAbstractItemView, QApplication, QFileDialog,
                         QMainWindow, QTabWidget)
from PyQt4.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt4.QtGui import QTableView,QApplication,QTableWidgetItem
import mysql.connector as mc
from ui_login import *
from ui_admin import *
import Login

global mydb
global cursor
class a_MainWindow(QtGui.QMainWindow,admin_MainWindow):

    def __init__(self, parent=None):
        global mydb 
        global cursor
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.centerOnScreen()
        self.btn_ejecutar.clicked.connect(self.Ejecutar)
        self.btn_borrar.clicked.connect(self.Borrar)
        self.btn_salir.clicked.connect(self.Salir)

        mydb = mc.connect(
           host="localhost",
           user= "root",
           password= "",
           database="BANCO"
           )
        cursor = mydb.cursor()
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'BANCO'")
        # Read and print tables
        for table in [tables[0] for tables in cursor.fetchall()]:
            self.lista_tablas.addItem(table)
            
      
        self.lista_tablas.itemClicked.connect(self.Atributos)


    def Atributos(self,item):
        global cursor
        self.lista_atributos.clear()
        tabla = str(item.text())
        c = "SELECT COLUMN_NAME  FROM INFORMATION_SCHEMA.COLUMNS  WHERE TABLE_NAME = '"+tabla+"'  ORDER BY ORDINAL_POSITION"
        print c
        cursor.execute(c)
        for x in [tables[0] for tables in cursor.fetchall()]:
           
            self.lista_atributos.addItem(str(x))
            print x

    def Ejecutar(self):
        global mydb
        self.Borrar()
        consul = str(self.text_consulta.toPlainText())
        cursor = mydb.cursor()
        cursor.execute(consul)
        columnas = cursor.column_names
        self.tableWidget.setColumnCount(len(columnas))
        self.tableWidget.setHorizontalHeaderLabels(columnas)
        fila = 0
        row = cursor.fetchone()
        while row is not None:
            col = 0
            self.tableWidget.insertRow(fila)
            for x in row:
                
                self.tableWidget.setItem(fila, col, QtGui.QTableWidgetItem(str(x)))
                col += 1
            fila += 1
            row = cursor.fetchone()
        
    def Borrar(self):
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

    def Salir(self):
        global mydb
        self.dialog = Login.MainWindow(self)
        self.dialog.show()
        self.hide()  
        mydb.close()     

    def centerOnScreen (self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())     