import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Users import Users

qtcreator_file  = "ui/users.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class UsersWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data)
        self.btnUpdate.clicked.connect(self.update_data)
        self.txtUsername.returnPressed.connect(self.search_data)
        self.btnCancel.clicked.connect(self.clear_entry)
        self.disableButton()

    # search data users
    def search_data(self):
        try:
            usr = Users()
            username=self.txtUsername.text()

            # search process
            result = usr.getByUsername(username)
            a = usr.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.disableButton()

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # save data for usr
    def update_data(self, MainWindow):
        try:
            usr = Users()
            username=self.txtUsername.text()
            role_name=self.cboRole.currentText()

            # set values to classes usr
            usr.role_name=role_name
            a = usr.updateByUsername(username)
            if(a>0):
                self.messagebox("SUKSES", "Data User Diperbarui")
            else:
                self.messagebox("GAGAL", "Data User Gagal Diperbarui")
            self.clear_entry(self) # Clear Entry Form

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def TampilData(self,result):
        self.txtUsername.setText(result[0])
        self.cboRole.setCurrentText(result[1])
        self.enableButton()

    def clear_entry(self, MainWindow):
        self.txtUsername.setText('')
        self.cboRole.setCurrentText('')
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
    window = UsersWindow()
    window.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = UsersWindow()
