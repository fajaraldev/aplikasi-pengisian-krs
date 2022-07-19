import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Dosen import Dosen

qtcreator_file  = "ui/dosen.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class DosenwaWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data)
        self.btnSimpan.clicked.connect(self.save_data)
        self.txtNidn.returnPressed.connect(self.search_data)
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def select_data(self):
        try:
            dsn = Dosen()

            # Get all
            result = dsn.getAllData()

            self.gridDosen.setHorizontalHeaderLabels(['NIDN', 'Nama', 'JK', 'TTL', 'Alamat', 'Email', 'Telepon'])
            self.gridDosen.setRowCount(0)


            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridDosen.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridDosen.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # search data for Dosen
    def search_data(self):
        try:
            dsn = Dosen()
            nidn=self.txtNidn.text()

            # search process
            result = dsn.getByNidn(nidn)
            a = dsn.affected
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

    # save data for Dosen
    def save_data(self, MainWindow):
        try:
            dsn = Dosen()
            nidn=self.txtNidn.text()
            nama=self.txtNama.text()
            jk=self.cboJk.currentText()
            ttl=self.txtTtl.text()
            alamat=self.txtAlamat.text()
            email=self.txtEmail.text()
            telepon=self.txtTelepon.text()

            if(self.edit_mode==False):
                dsn.nidn=nidn
                dsn.nama=nama
                dsn.jk=jk
                dsn.ttl=ttl
                dsn.alamat=alamat
                dsn.email=email
                dsn.telepon=telepon
                a = dsn.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Dosen Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Dosen Gagal Tersimpan")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                dsn.nama=nama
                dsn.jk=jk
                dsn.ttl=ttl
                dsn.alamat=alamat
                dsn.email=email
                dsn.telepon=telepon
                a = dsn.updateByNidn(nidn)
                if(a>0):
                    self.messagebox("SUKSES", "Data Dosen Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Dosen Gagal Diperbarui")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")


        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    # delete data for Dosen
    def delete_data(self, MainWindow):
        try:
            dsn = Dosen()
            nidn=self.txtNidn.text()

            if(self.edit_mode==True):
                a = dsn.deleteByNidn(nidn)
                if(a>0):
                    self.messagebox("SUKSES", "Data Dosen Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Dosen Gagal Dihapus")

                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")


        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        self.txtNidn.setText(result[0])
        self.txtNama.setText(result[1])
        self.cboJk.setCurrentText(result[2])
        self.txtTtl.setText(result[3])
        self.txtAlamat.setText(result[4])
        self.txtEmail.setText(result[5])
        self.txtTelepon.setText(result[6])

        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
        self.btnHapus.setStyleSheet("background-color : red")

    def clear_entry(self, MainWindow):
        self.txtNidn.setText("")
        self.txtNama.setText("")
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
    window = DosenwaWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = DosenwaWindow()
