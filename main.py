import sys, sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QRadioButton
from PyQt5 import uic

class movSrch(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('genre_search.ui', self)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        result = self.do_query('select title from genres order by title')
        for i in result:
            self.comboBox.addItem(i[0])

    def do_query(self, sql_txt):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute(sql_txt).fetchall()
        con.close()
        return result

    def selectionchange(self):
        sql_txt = 'SELECT f.id, f.title, f.year, f.duration FROM Films as f ' +\
            'where f.genre in(select id from genres where title = "' + \
            self.comboBox.currentText() + '")order by f.id'
        result = self.do_query(sql_txt)
        self.statusBar().showMessage('В выбранном жанре ' + str(len(result)) + ' фильмов')
        self.tableWidget.clearContents()
        if len(result) > 0:
            self.tableWidget.setRowCount(len(result))
            for r in range(len(result)):
                for i in range(4):
                    item = QTableWidgetItem()
                    item.setText(str(result[r][i]))
                    self.tableWidget.setItem(r, i, item)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex = movSrch()
    ex.show()
    sys.exit(app.exec())
