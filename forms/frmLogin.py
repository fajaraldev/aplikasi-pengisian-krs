import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from forms.MainWindow import MainWindow
from classes.Users import Users as Login

qtcreator_file  = "ui/login.ui" # File Design Tampilan Dashboard
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Event Setup
        self.btnSubmit.clicked.connect(self.app_login) # ketika klik tombol submit

    def app_login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        usr.validate(username,password)

        if(usr.currentUser[0]==True): # Login berhasil
            self.close()
            dashboard.show()
            self.messagebox("Info","Login Berhasil")
        else: # login gagal
            self.messagebox("Info","Maaf login gagal")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    usr = Login()
    window = LoginWindow()
    dashboard = MainWindow()
    window.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    usr = Login()
    window = LoginWindow()
    dashboard = MainWindow()
