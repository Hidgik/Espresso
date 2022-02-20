import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel, QLineEdit, QWidget, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from database import Person


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('pyfilename.py', self)
        conn = sqlite3.connect('coffee.db')
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
        self.c = AddCoffee()
        self.c.show()
        self.hide()


class AddCoffee(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        conn = sqlite3.connect('coffee.db')
        self.cur = conn.cursor()
        self.result = self.cur.execute("""SELECT * FROM Person""").fetchall()
        self.btn.clicked.connect(self.run)

    def run(self):
        a = Person.create(id=len(self.result)+1, name=self.le.text(), d=self.le2.text(), gro_gra=self.le3.text(), name2=self.le4.text(), price=self.sb.value(), v=self.dsb.value())
        a.save()
        self.c = MyWidget()
        self.c.show()
        self.hide()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    w = MyWidget()
    w.show()
    sys.exit(app.exec())