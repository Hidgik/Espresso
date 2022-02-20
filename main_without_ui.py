import sys
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from peewee import *
import os

fullname = os.path.join("data", "coffee.db")
db = SqliteDatabase(fullname)  


class Person(Model):
    id = IntegerField()
    name = CharField()
    d = CharField()
    gro_gra = CharField()
    name2 = CharField()
    price = IntegerField()
    v = IntegerField()

    class Meta:
        database = db

class My_Widget(object):
    def setupUi(self, Form):
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.resize(800, 598)
        self.btn = QtWidgets.QPushButton(self.Form)
        self.btn.setGeometry(QtCore.QRect(210, 0, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.table = QtWidgets.QTableWidget(self.Form)
        self.table.setGeometry(QtCore.QRect(0, 50, 801, 551))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        conn = sqlite3.connect('data\coffee.db')
        self.cur = conn.cursor()
        self.result = self.cur.execute("""SELECT * FROM Person""").fetchall()
        self.table.setRowCount(len(self.result))
        self.table.setColumnCount(7)
        names = ["Id", "Название", "Степень обжарки", "Молотый/в зёрнах", "Описание вкуса", "Цена", "Объём упаковки"]
        self.table.setHorizontalHeaderLabels(names)
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.btn.clicked.connect(self.run)

    def run(self):
        self.f = QtWidgets.QWidget()
        self.c = AddCoffee()
        self.c.setupUi(self.f)
        self.f.show()
        self.Form.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "Добавить кофе"))


class AddCoffee(object):
    def setupUi(self, Form):
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.resize(400, 360)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 141, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l2.setObjectName("l2")
        self.verticalLayout.addWidget(self.l2)
        self.l3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l3.setObjectName("l3")
        self.verticalLayout.addWidget(self.l3)
        self.l1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l1.setObjectName("l1")
        self.verticalLayout.addWidget(self.l1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(200, 10, 160, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.le.setObjectName("le")
        self.verticalLayout_2.addWidget(self.le)
        self.le3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.le3.setObjectName("le3")
        self.verticalLayout_2.addWidget(self.le3)
        self.le2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.le2.setObjectName("le2")
        self.verticalLayout_2.addWidget(self.le2)
        self.le4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.le4.setObjectName("le4")
        self.verticalLayout_2.addWidget(self.le4)
        self.sb = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.sb.setObjectName("sb")
        self.verticalLayout_2.addWidget(self.sb)
        self.dsb = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.dsb.setDecimals(1)
        self.dsb.setObjectName("dsb")
        self.verticalLayout_2.addWidget(self.dsb)
        self.btn = QtWidgets.QPushButton(self.Form)
        self.btn.setGeometry(QtCore.QRect(90, 310, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        
        conn = sqlite3.connect('data\coffee.db')
        self.cur = conn.cursor()
        self.result = self.cur.execute("""SELECT * FROM Person""").fetchall()
        self.btn.clicked.connect(self.run)

    def run(self):
        a = Person.create(id=len(self.result)+1, name=self.le.text(), d=self.le2.text(), gro_gra=self.le3.text(), name2=self.le4.text(), price=self.sb.value(), v=self.dsb.value())
        a.save()
        self.f = QtWidgets.QWidget()
        self.c = My_Widget()
        self.c.setupUi(self.f)
        self.f.show()
        self.Form.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.l2.setText(_translate("Form", "Название"))
        self.l3.setText(_translate("Form", "Степень обжарки"))
        self.l1.setText(_translate("Form", "Молотый/в зёрнах"))
        self.label_5.setText(_translate("Form", "Описание вкуса"))
        self.label_4.setText(_translate("Form", "Цена"))
        self.label_6.setText(_translate("Form", "Объём"))
        self.btn.setText(_translate("Form", "Добавить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = My_Widget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
