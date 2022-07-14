import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Matakuliah import Matakuliah
from classes.Prodi import Prodi
from classes.Krs import Krs
from classes.Users import userInfo
from GlobalVariable import GlobalVariable

qtcreator_file  = "ui/krs.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class KrsWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.txtNimPencarian.returnPressed.connect(self.select_data)
        self.btnCariKrsByNim.clicked.connect(self.select_data)
        self.txtIdKrs.returnPressed.connect(self.search_data)
        self.btnCariKrsById.clicked.connect(self.search_data)
        self.btnCariMatakuliBySemester.clicked.connect(self.search_matakuliah)
        self.btnSimpan.clicked.connect(self.save_data)
        self.btnClear.clicked.connect(self.clear_entry)
        # self.btnHapus.clicked.connect(self.delete_data)

        self.edit_mode=""
        self.disableButton()

    def select_data(self):
        try:
            krs = Krs()

            # Get all data krs
            nim=self.txtNimPencarian.text()
            result = krs.getAllDataByNim(nim)

            self.gridKrs.setHorizontalHeaderLabels(['Id','NIM', 'Tahun Ajaran','Semester','Matakuliah','Hari','Waktu','Ruang'])
            self.gridKrs.setRowCount(0)

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridKrs.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridKrs.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # search data matakuliah
    def search_matakuliah(self):
        try:
            username = self.txtNim.text()
            semester = self.cboSemester.currentText()
            g_var.getAllMatakuliahByUsernameAndSemester(username, semester)
            self.cboMatakuliah.clear() # reset data cbo matakuliah
            a = g_var.affected
            if(a>0):
                # set data to cboProdi form
                for x in g_var.matakuliah:
                  self.cboMatakuliah.addItem(x[1])
            else:
                self.messagebox("INFO", "Data Matakuliah tidak tersedia!")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # search data for krs
    def search_data(self):
        try:
            krs = Krs()
            id=self.txtIdKrs.text()

            # search process
            result = krs.getAllInfoKrsById(id)
            a = krs.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNim.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False)
                self.btnHapus.setStyleSheet("color:black;background-color : grey")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # save data for krs
    def save_data(self, MainWindow):
        try:
            krs = Krs()
            id=self.txtIdKrs.text()

            # get value from ui
            nim=self.txtNim.text()
            ajaran=self.txtAjaran.text()
            semester=self.cboSemester.currentText()
            matakuliah=self.cboMatakuliah.currentText()
            hari=self.cboHari.currentText()
            waktu=self.txtWaktu.text()
            ruang=self.txtRuang.text()

            if(self.edit_mode==False):
                krs.getProdiByNim(nim)
                krs.nim=nim
                krs.ajaran=ajaran
                krs.semester=semester
                krs.matakuliah=matakuliah
                krs.hari=hari
                krs.waktu=waktu
                krs.ruang=ruang
                a = krs.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data KRS Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data KRS Gagal Tersimpan")

                self.clear_entry(self)
                self.select_data()

            elif(self.edit_mode==True):
                krs.getProdiByNim(nim)
                krs.nim=nim
                krs.ajaran=ajaran
                krs.semester=semester
                krs.matakuliah=matakuliah
                krs.semester=semester
                krs.hari=hari
                krs.waktu=waktu
                krs.ruang=ruang
                a = krs.updateByIdKrs(id)
                if(a>0):
                  self.messagebox("SUKSES", "Data KRS Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data KRS Gagal Diperbarui")

                self.clear_entry(self)
                self.select_data()
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def TampilData(self,result):
        self.cboMatakuliah.clear() # reset data cbo matakuliah

        self.txtIdKrs.setText(str(result[0]))
        self.txtNim.setText(result[1])
        self.txtAjaran.setText(result[2])
        self.cboSemester.setCurrentText(str(result[3]))
        self.cboMatakuliah.addItem(result[4])
        self.cboMatakuliah.setCurrentText(result[4])
        self.cboHari.setCurrentText(result[5])
        self.txtWaktu.setText(result[6])
        self.txtRuang.setText(result[7])
        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.enableButton()

    def clear_entry(self, MainWindow):
        self.txtIdKrs.setText('')
        self.txtNim.setText('')
        self.txtAjaran.setText('')
        self.cboSemester.setCurrentText('')
        self.cboMatakuliah.clear() # reset data cbo matakuliah
        self.cboMatakuliah.setCurrentText('')
        self.cboHari.setCurrentText('')
        self.txtWaktu.setText('')
        self.txtRuang.setText('')
        self.disableButton()

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

    def enableButton(self):
        self.btnSimpan.setEnabled(True)
        self.btnSimpan.setStyleSheet("color:white;  background-color : blue")
        self.btnHapus.setEnabled(True)
        self.btnHapus.setStyleSheet("color:white; background-color : red")

    def disableButton(self):
        self.btnSimpan.setEnabled(False)
        self.btnSimpan.setStyleSheet("color:black;background-color : grey")
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    g_var = GlobalVariable()
    window = KrsWindow()
    window.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    g_var = GlobalVariable()
    window = KrsWindow()
