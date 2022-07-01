import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from Mahasiswa import Mahasiswa
from Prodi import Prodi

qtcreator_file  = "mahasiswa.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MahasiswaWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data)
        self.btnCariProdi.clicked.connect(self.search_data_prodi)
        self.btnSimpan.clicked.connect(self.save_data)
        self.txtNim.returnPressed.connect(self.search_data)
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def select_data(self):
        try:
            mhs = Mahasiswa()

            # Get all
            result = mhs.getAllData()

            self.gridMahasiswa.setHorizontalHeaderLabels(['NIM', 'Nama', 'Prodi', 'JK', 'TTL', 'Alamat', 'Email', 'Telepon'])
            self.gridMahasiswa.setRowCount(0)


            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridMahasiswa.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridMahasiswa.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data_prodi(self):
        try:
            prd = Prodi()
            kode_prodi=self.txtKodeProdi.text()
            # search process
            result = prd.getByKodeProdi(kode_prodi)
            a = prd.affected
            if(a>0):
                self.txtProdi.setText(prd.prodi.strip())
            else:
                self.messagebox("INFO", "Data Prodi tidak ditemukan")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # search data for mahasiswa
    def search_data(self):
        try:
            mhs = Mahasiswa()
            nim=self.txtNim.text()

            # search process
            result = mhs.getByNim(nim)
            a = mhs.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNama.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # save data for mahasiswa
    def save_data(self, MainWindow):
        try:
            mhs = Mahasiswa()
            nim=self.txtNim.text()
            nama=self.txtNama.text()
            prodi=self.txtKodeProdi.text()
            jk=self.cboJk.currentText()
            ttl=self.txtTtl.text()
            alamat=self.txtAlamat.text()
            email=self.txtEmail.text()
            telepon=self.txtTelepon.text()

            if(self.edit_mode==False):
                mhs.nim=nim
                mhs.nama=nama
                mhs.prodi=prodi
                mhs.jk=jk
                mhs.ttl=ttl
                mhs.alamat=alamat
                mhs.email=email
                mhs.telepon=telepon
                a = mhs.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Mahasiswa Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Mahasiswa Gagal Tersimpan")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                mhs.nama=nama
                mhs.prodi=prodi
                mhs.jk=jk
                mhs.ttl=ttl
                mhs.alamat=alamat
                mhs.email=email
                mhs.telepon=telepon
                a = mhs.updateByNim(nim)
                if(a>0):
                    self.messagebox("SUKSES", "Data Mahasiswa Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Mahasiswa Gagal Diperbarui")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")


        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    # delete data for mahasiswa
    def delete_data(self, MainWindow):
        try:
            mhs = Mahasiswa()
            nim=self.txtNim.text()

            if(self.edit_mode==True):
                a = mhs.deleteByNim(nim)
                if(a>0):
                    self.messagebox("SUKSES", "Data Mahasiswa Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Mahasiswa Gagal Dihapus")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")


        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        self.txtNim.setText(result[0])
        self.txtNama.setText(result[1])
        self.txtKodeProdi.setText(result[2])
        self.cboJk.setCurrentText(result[3])
        self.txtTtl.setText(result[4])
        self.txtAlamat.setText(result[5])
        self.txtEmail.setText(result[6])
        self.txtTelepon.setText(result[7])

        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
        self.btnHapus.setStyleSheet("background-color : red")

    def clear_entry(self, MainWindow):
        self.txtNim.setText("")
        self.txtNama.setText("")
        self.txtKodeProdi.setText("")
        self.cboJk.setCurrentText("")
        self.txtTtl.setText("")
        self.txtAlamat.setText("")
        self.txtEmail.setText("")
        self.txtTelepon.setText("")

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
    window = MahasiswaWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = MahasiswaWindow()
