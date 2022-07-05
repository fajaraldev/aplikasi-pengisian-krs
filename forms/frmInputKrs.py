import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Matakuliah import Matakuliah
from classes.Prodi import Prodi
from classes.Krs import Krs
from GlobalVariable import GlobalVariable

qtcreator_file  = "ui/inputKrs.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class InputKrsWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnSimpan.clicked.connect(self.save_data)
        self.btnClear.clicked.connect(self.clear_entry)

        # set data to cboMatakuliah form
        for x in g_var.matakuliah:
          self.cboMatakuliah.addItem(x[1], x[0])

    def select_data(self):
        try:
            krs = Krs()

            # Get all
            result = krs.getAllData()

            self.gridKrs.setHorizontalHeaderLabels(['Id', 'Tahun Ajaran','Semester','Matakuliah','Hari','Waktu','Ruang'])
            self.gridKrs.setRowCount(0)


            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridKrs.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridKrs.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # save data for matakuliah
    def save_data(self, MainWindow):
        try:
            krs = Krs()
            ajaran=self.txtAjaran.text()
            semester=self.cboSemester.currentText()
            matakuliah=self.cboMatakuliah.currentText()
            semester=self.cboSemester.currentText()
            hari=self.cboHari.currentText()
            waktu=self.txtWaktu.text()
            ruang=self.txtRuang.text()

            # set values to classes krs
            krs.ajaran=ajaran
            krs.semester=semester
            krs.matakuliah=matakuliah
            krs.semester=semester
            krs.hari=hari
            krs.waktu=waktu
            krs.ruang=ruang
            a = krs.simpan()
            if(a>0):
                self.messagebox("SUKSES", "Data Krs Tersimpan")
            else:
                self.messagebox("GAGAL", "Data Krs Gagal Tersimpan")

            self.clear_entry(self) # Clear Entry Form
            self.select_data() # Reload Datagrid


        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def clear_entry(self, MainWindow):
        self.txtAjaran.setText('')
        self.cboSemester.setCurrentText('')
        self.cboMatakuliah.setCurrentText('')
        self.cboSemester.setCurrentText('')
        self.cboHari.setCurrentText('')
        self.txtWaktu.setText('')
        self.txtRuang.setText('')

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    g_var = GlobalVariable()
    g_var.getAllMatakuliahByProdi("A01")
    window = InputKrsWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    g_var = GlobalVariable()
    g_var.getAllMatakuliahByProdi("A01")
    window = InputKrsWindow()
