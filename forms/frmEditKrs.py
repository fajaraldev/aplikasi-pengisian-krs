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

qtcreator_file  = "ui/editKrs.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class EditKrsWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCariKrs.clicked.connect(self.search_data)
        self.btnCariMatakuliBySemesterah.clicked.connect(self.search_matakuliah)
        self.btnUpdate.clicked.connect(self.update_data)
        self.txtIdKrs.returnPressed.connect(self.search_data)
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnShowAllData.clicked.connect(self.select_data)
        # self.btnHapus.clicked.connect(self.delete_data)
        self.disableButton()

    def select_data(self):
        try:
            krs = Krs()

            # Get all
            result = krs.getAllDataByUsername(userInfo[1])

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

    # search data matakuliah
    def search_matakuliah(self):
        try:
            username = userInfo[1]
            semester = self.cboSemester.currentText()
            g_var.getAllMatakuliahByProdiAndSemester(username, semester)
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
            result = krs.getByIdKrs(id)
            a = krs.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.disableButton()

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # save data for krs
    def update_data(self, MainWindow):
        try:
            krs = Krs()
            id=self.txtIdKrs.text()

            # get value from ui
            ajaran=self.txtAjaran.text()
            semester=self.cboSemester.currentText()
            matakuliah=self.cboMatakuliah.currentText()
            semester=self.cboSemester.currentText()
            hari=self.cboHari.currentText()
            waktu=self.txtWaktu.text()
            ruang=self.txtRuang.text()

            # set values to classes krs
            krs.getUserNimAndProdi(userInfo[1]) #userInfo[1] = username
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

            self.clear_entry(self) # Clear Entry Form
            self.select_data() # Reload Datagrid

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def TampilData(self,result):
        self.cboMatakuliah.clear() # reset data cbo matakuliah

        self.txtIdKrs.setText(str(result[0]))
        self.txtAjaran.setText(result[1])
        self.cboSemester.setCurrentText(str(result[2]))
        self.cboMatakuliah.addItem(result[3])
        self.cboMatakuliah.setCurrentText(result[3])
        self.cboHari.setCurrentText(result[4])
        self.txtWaktu.setText(result[5])
        self.txtRuang.setText(result[6])
        self.enableButton()

    def clear_entry(self, MainWindow):
        self.txtIdKrs.setText('')
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
        self.btnUpdate.setEnabled(True)
        self.btnUpdate.setStyleSheet("color:white;  background-color : blue")
        self.btnHapus.setEnabled(True)
        self.btnHapus.setStyleSheet("color:white; background-color : red")

    def disableButton(self):
        self.btnUpdate.setEnabled(False)
        self.btnUpdate.setStyleSheet("color:black;background-color : grey")
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    g_var = GlobalVariable()
    window = EditKrsWindow()
    window.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    g_var = GlobalVariable()
    window = EditKrsWindow()
