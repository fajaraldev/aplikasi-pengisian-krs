import sys
from PyQt5.QtWidgets import *
from forms.frmLogin import LoginWindow

__author__ = 'umc'

def main():
    a = QApplication(sys.argv)
    a.setQuitOnLastWindowClosed(True)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(a.exec_())

main()
