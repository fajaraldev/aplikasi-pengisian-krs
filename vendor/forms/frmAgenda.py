import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QRadioButton
from classes.Agenda import Agenda

qtcreator_file  = "ui/agenda.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class AgendaWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtKodeAgenda.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox kode_agenda
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")
        self.select_data()

    def select_data(self):
        try:
            agn = Agenda()

            # Get all
            result = agn.getAllData()

            self.gridAgenda.setHorizontalHeaderLabels(['ID', 'Kode Agenda', 'Nama MK', 'SKS', 'Nama Dosen', 'Hari', 'Kode Ruangan', 'Waktu'])
            self.gridAgenda.setRowCount(0)

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridAgenda.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridAgenda.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:
            kode_agenda=self.txtKodeAgenda.text()
            agn = Agenda()
            # search process
            result = agn.getByKodeAgenda(kode_agenda)
            a = agn.affected
            if(a!=0):
                self.txtNamaMk.setText(agn.nama_matakuliah.strip())
                self.txtSks.setText(agn.sks.strip())
                self.txtNamaDosen.setText(agn.nama_dosen.strip())
                self.txtHari.setText(agn.hari.strip())
                self.txtKodeRuangan.setText(agn.kode_ruangan.strip())
                self.txtWaktu.setText(agn.waktu.strip())
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("background-color : red")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNamaMk.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self):
        try:
            agn = Agenda()
            kode_agenda=self.txtKodeAgenda.text()
            nama_matakuliah=self.txtNamaMk.text()
            sks=self.txtSks.text()
            nama_dosen=self.txtNamaDosen.text()
            hari=self.txtHari.text()
            kode_ruangan=self.txtKodeRuangan.text()
            waktu=self.txtWaktu.text()

            if(self.edit_mode==False):
                agn.kode_agenda = kode_agenda
                agn.nama_matakuliah = nama_matakuliah
                agn.sks = sks
                agn.nama_dosen = nama_dosen
                agn.hari = hari
                agn.kode_ruangan = kode_ruangan
                agn.waktu = waktu

                a = agn.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Agenda Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Agenda Gagal Tersimpan")

                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                agn.kode_agenda = kode_agenda
                agn.nama_matakuliah = nama_matakuliah
                agn.sks = sks
                agn.nama_dosen = nama_dosen
                agn.hari = hari
                agn.kode_ruangan = kode_ruangan
                agn.waktu = waktu
                a = agn.updateByKodeAgenda(kode_agenda)
                if(a>0):
                    self.messagebox("SUKSES", "Data Agenda Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Agenda Gagal Diperbarui")

                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")


        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self):
        try:
            agn = Agenda()
            kode_agenda=self.txtKodeAgenda.text()

            if(self.edit_mode==True):
                a = agn.deleteByKodeAgenda(kode_agenda)
                if(a>0):
                    self.messagebox("SUKSES", "Data Agenda Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Agenda Gagal Dihapus")

                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")


        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self):
        self.txtKodeAgenda.setText("")
        self.txtNamaMk.setText("")
        self.txtSks.setText("")
        self.txtNamaDosen.setText("")
        self.txtHari.setText("")
        self.txtKodeRuangan.setText("")
        self.txtWaktu.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AgendaWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
