import sys, sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QRadioButton
from PyQt5 import uic

class movSrch(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.selectionchange)

    def do_query(self, sql_txt):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute(sql_txt).fetchall()
        con.close()
        return result

    def selectionchange(self):
        sql_txt = 'select * from coffee_sort order by id'
        result = self.do_query(sql_txt)
        self.statusBar().showMessage('Отобрано ' + str(len(result)) + ' записей')
        self.tableWidget.clearContents()
        if len(result) > 0:
            self.tableWidget.setRowCount(len(result))
            for r in range(len(result)):
                for i in range(7):
                    item = QTableWidgetItem()
                    item.setText(str(result[r][i]))
                    self.tableWidget.setItem(r, i, item)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex = movSrch()
    ex.show()
    sys.exit(app.exec())
