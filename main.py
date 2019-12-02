import sys, sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Program')
        self.loadTable()

    def loadTable(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        result = cur.execute("select * from Кофе").fetchall()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([description[0] for description in cur.description])
        self.table.setRowCount(0)
        for i, row in enumerate(result):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j in range(7):
                self.table.setItem(i, j, QTableWidgetItem(str(row[j])))
        self.table.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
