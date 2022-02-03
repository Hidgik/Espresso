import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel, QLineEdit, QWidget, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        conn = sqlite3.connect('coffee.db')
        self.cur = conn.cursor()
        self.result = self.cur.execute("""SELECT * FROM Person""").fetchall()
        self.table.setRowCount(len(self.result))
        self.table.setColumnCount(7)
        #self.table.setGeometry(0, 50, 1000, 550)
        names = ["Id", "Название", "Степень обжарки", "Молотый/в зёрнах", "Описание вкуса", "Цена", "Объём упаковки"]
        self.table.setHorizontalHeaderLabels(names)
        print(self.result)
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.run()

    def run(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    w = MyWidget()
    w.show()
    sys.exit(app.exec())