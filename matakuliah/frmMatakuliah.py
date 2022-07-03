import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from Matakuliah import Matakuliah
from Prodi import Prodi
from GlobalVariable import prodi

qtcreator_file  = "matakuliah.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MatakuliahWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data)
        self.btnSimpan.clicked.connect(self.save_data)
        self.txtKodeMatakuliah.returnPressed.connect(self.search_data)
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

        # set data to cboProdi form
        for x in prodi:
          self.cboProdi.addItem(x[1], x[0])

    def select_data(self):
        try:
            mk = Matakuliah()

            # Get all
            result = mk.getAllData()

            self.gridMatakuliah.setHorizontalHeaderLabels(['Kode MK', 'Matakuliah', 'SKS', 'Prodi', 'Semester'])
            self.gridMatakuliah.setRowCount(0)


            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridMatakuliah.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridMatakuliah.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # search data for matakuliah
    def search_data(self):
        try:
            mk = Matakuliah()
            kode_matakuliah=self.txtKodeMatakuliah.text()

            # search process
            result = mk.getByKodeMatakuliah(kode_matakuliah)
            a = mk.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtMatakuliah.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False)
                self.btnHapus.setStyleSheet("color:black;background-color : grey")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # save data for matakuliah
    def save_data(self, MainWindow):
        try:
            mk = Matakuliah()
            kode_matakuliah=self.txtKodeMatakuliah.text()
            matakuliah=self.txtMatakuliah.text()
            sks=self.cboSks.currentText()
            prodi=self.cboProdi.currentText()
            semester=self.cboSemester.currentText()

            if(self.edit_mode==False):
                mk.kode_matakuliah=kode_matakuliah
                mk.matakuliah=matakuliah
                mk.sks=sks
                mk.prodi=prodi
                mk.semester=semester
                a = mk.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Matakuliah Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Matakuliah Gagal Tersimpan")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                mk.kode_matakuliah=kode_matakuliah
                mk.matakuliah=matakuliah
                mk.sks=sks
                mk.prodi=prodi
                mk.semester=semester
                a = mk.updateByKodeMatakuliah(kode_matakuliah)
                if(a>0):
                    self.messagebox("SUKSES", "Data Matakuliah Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Matakuliah Gagal Diperbarui")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")


        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    # delete data for matakuliah
    def delete_data(self, MainWindow):
        try:
            mk = Matakuliah()
            kode_matakuliah=self.txtKodeMatakuliah.text()

            if(self.edit_mode==True):
                a = mk.deleteByKodeMatakuliah(kode_matakuliah)
                if(a>0):
                    self.messagebox("SUKSES", "Data Matakuliah Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Matakuliah Gagal Dihapus")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")


        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        self.txtKodeMatakuliah.setText(result[0])
        self.txtMatakuliah.setText(result[1])
        self.cboSks.setCurrentText(str(result[2]))
        self.cboProdi.setCurrentText(result[3])
        self.cboSemester.setCurrentText(str(result[4]))

        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
        self.btnHapus.setStyleSheet("background-color : red")

    def clear_entry(self, MainWindow):
        self.txtKodeMatakuliah.setText('')
        self.txtMatakuliah.setText('')
        self.cboSks.setCurrentText('')
        self.cboProdi.setCurrentText('')
        self.cboSemester.setCurrentText('')

        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MatakuliahWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = MatakuliahWindow()
