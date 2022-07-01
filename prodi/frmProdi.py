import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from Prodi import Prodi

qtcreator_file  = "prodi.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class ProdiWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data)
        self.btnSimpan.clicked.connect(self.save_data)
        self.txtKodeProdi.returnPressed.connect(self.search_data)
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def select_data(self):
        try:
            prd = Prodi()

            # Get all
            result = prd.getAllData()

            self.gridProdi.setHorizontalHeaderLabels(['Kode Prodi', 'Prodi'])
            self.gridProdi.setRowCount(0)


            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridProdi.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridProdi.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:
            prd = Prodi()
            kode_prodi=self.txtKodeProdi.text()

            # search process
            result = prd.getByKodeProdi(kode_prodi)
            a = prd.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtProdi.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            prd = Prodi()
            kode_prodi=self.txtKodeProdi.text()
            prodi=self.txtProdi.text()

            if(self.edit_mode==False):
                prd.kode_prodi=kode_prodi
                prd.prodi=prodi
                a = prd.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Prodi Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Prodi Gagal Tersimpan")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                prd.kode_prodi=kode_prodi
                prd.prodi=prodi
                a = prd.updateByKodeProdi(kode_prodi)
                if(a>0):
                    self.messagebox("SUKSES", "Data Prodi Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Prodi Gagal Diperbarui")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")


        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def delete_data(self, MainWindow):
        try:
            prd = Prodi()
            kode_prodi=self.txtKodeProdi.text()

            if(self.edit_mode==True):
                a = prd.deleteByKodeProdi(kode_prodi)
                if(a>0):
                    self.messagebox("SUKSES", "Data Prodi Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Prodi Gagal Dihapus")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")


        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        self.txtKodeProdi.setText(result[0])
        self.txtProdi.setText(result[1])

        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
        self.btnHapus.setStyleSheet("background-color : red")

    def clear_entry(self, MainWindow):
        self.txtKodeProdi.setText("")
        self.txtProdi.setText("")

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
    window = ProdiWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = ProdiWindow()
