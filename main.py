import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QTableWidgetItem, QInputDialog
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Program')
        self.load.clicked.connect(self.loadTable)
        self.red.clicked.connect(self.runedit)
        self.modified = {}
        self.titles = None

    def loadTable(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        result = cur.execute("select * from Кофе").fetchall()
        self.table.setColumnCount(7)
        self.titles = [description[0] for description in cur.description]
        self.table.setHorizontalHeaderLabels(self.titles)
        self.table.setRowCount(0)
        for i, row in enumerate(result):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j in range(7):
                self.table.setItem(i, j, QTableWidgetItem(str(row[j])))
        self.table.resizeColumnsToContents()

    def runedit(self):
        self.sec = Edit()
        self.sec.show()


class Edit(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle('Program')
        self.table.itemChanged.connect(self.item_changed)
        self.add.clicked.connect(self.runadd)
        self.delet.clicked.connect(self.rundel)
        self.save.clicked.connect(self.runsave)
        self.con = sqlite3.connect('coffee.db')
        self.modified = {}
        self.titles = None
        self.loadTable()

    def item_changed(self, item):
        self.modified[(item.row(), self.titles[item.column()])] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            for row, col in self.modified.keys():
                que = "UPDATE Кофе SET\n"
                que += "'{}' = '{}'\n".format(col, self.modified.get((row, col)))
                que += "WHERE id = {}".format(row + 1)
                cur.execute(que)
            self.con.commit()

    def loadTable(self):
        self.save_results()
        cur = self.con.cursor()
        result = cur.execute("select * from Кофе").fetchall()
        self.table.setColumnCount(7)
        self.titles = [description[0] for description in cur.description]
        self.table.setHorizontalHeaderLabels(self.titles)
        self.table.setRowCount(0)
        for i, row in enumerate(result):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j in range(7):
                self.table.setItem(i, j, QTableWidgetItem(str(row[j])))
        self.table.resizeColumnsToContents()
        self.modified = {}

    def rundel(self):
        cur = self.con.cursor()
        i, ok = QInputDialog.getInt(self, "ID", "Выбрите ID", 1, 1, 1000000, 1)
        if ok:
            cur.execute("DELETE from Кофе where ID = ?", str(i))
        self.con.commit()
        self.loadTable()

    def runadd(self):
        cur = self.con.cursor()
        name, ok1 = QInputDialog.getText(self, "question", "Введите название сорта")
        step, ok2 = QInputDialog.getText(self, "question", "Введите степень обжарки")
        mol, ok3 = QInputDialog.getText(self, "question", "Введите молотый или в зернах кофе")
        dis, ok4 = QInputDialog.getText(self, "question", "Введите описание вкуса")
        price, ok5 = QInputDialog.getText(self, "question", "Введите цену")
        ob, ok6 = QInputDialog.getText(self, "question", "Введите объем упаковки")
        if ok1 and ok2 and ok3 and ok4 and ok5 and ok6:
            cur.execute("INSERT INTO Кофе('Название сорта', 'Степень обжарки', 'Молотый/в зернах',"
                        "'Описание вкуса', 'Цена', 'Объем упаковки') "
                        "VALUES(?, ?, ?, ?, ?, ?)",
                        (name, step, mol, dis, price, ob))
        self.con.commit()
        self.loadTable()

    def runsave(self):
        self.save_results()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
