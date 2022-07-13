import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Profile import Profile
from classes.Users import userInfo

qtcreator_file  = "ui/profile.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class ProfileWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.txtUsername.returnPressed.connect(self.search_data)
        self.btnCari.clicked.connect(self.search_data)
        self.btnUpdate.clicked.connect(self.update_data)
        self.btnCancel.clicked.connect(self.clear_entry)

        self.disableButton()

    # search data for mahasiswa
    def search_data(self):
        try:
            prf = Profile()
            username=userInfo[1]

            # search process
            result = prf.getByUsername(username)
            a = prf.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.disableButton()

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # save data for mahasiswa
    def update_data(self, MainWindow):
        try:
            prf = Profile()
            username=userInfo[1]
            nama=self.txtNama.text()
            jk=self.cboJk.currentText()
            ttl=self.txtTtl.text()
            alamat=self.txtAlamat.text()
            email=self.txtEmail.text()
            telepon=self.txtTelepon.text()

            # set values to classes profile
            prf.nama=nama
            prf.jk=jk
            prf.ttl=ttl
            prf.alamat=alamat
            prf.email=email
            prf.telepon=telepon
            a = prf.updateByUsername(username)
            if(a>0):
                self.messagebox("SUKSES", "Data Profile Diperbarui")
            else:
                self.messagebox("GAGAL", "Data Profile Gagal Diperbarui")

            self.clear_entry(self) # Clear Entry Form

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def TampilData(self,result):
        self.txtUsername.setText(result[0])
        self.txtNama.setText(result[1])
        self.cboProdi.addItem(result[2])
        self.cboProdi.setCurrentText(result[2])
        self.cboJk.setCurrentText(result[3])
        self.txtTtl.setText(result[4])
        self.txtAlamat.setText(result[5])
        self.txtEmail.setText(result[6])
        self.txtTelepon.setText(result[7])

        self.enableButton()

    def clear_entry(self, MainWindow):
        self.txtUsername.setText("")
        self.txtNama.setText("")
        self.cboProdi.clear()
        self.cboJk.setCurrentText("")
        self.txtTtl.setText("")
        self.txtAlamat.setText("")
        self.txtEmail.setText("")
        self.txtTelepon.setText("")

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
        self.btnCancel.setEnabled(True)
        self.btnCancel.setStyleSheet("color:white; background-color : red")

    def disableButton(self):
        self.btnUpdate.setEnabled(False)
        self.btnUpdate.setStyleSheet("color:black;background-color : grey")
        self.btnCancel.setEnabled(False)
        self.btnCancel.setStyleSheet("color:black;background-color : grey")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ProfileWindow()
    window.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = ProfileWindow()
