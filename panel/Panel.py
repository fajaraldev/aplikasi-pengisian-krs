from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmMahasiswa import MahasiswaWindow
from forms.frmMatakuliah import MatakuliahWindow
from forms.frmProdi import ProdiWindow
from forms.frmKrs import KrsWindow
from forms.frmInputKrs import InputKrsWindow
from forms.frmEditKrs import EditKrsWindow
from forms.frmUsers import UsersWindow
from forms.frmProfile import ProfileWindow

dock = QtWidgets.QDockWidget()

def child_panels(self):
    matakuliah_panel(self)
    mahasiswa_panel(self)
    prodi_panel(self)
    krs_panel(self)
    input_krs_panel(self)
    edit_krs_panel(self)
    users_panel(self)
    profile_panel(self)

# Mahasiswa
def mahasiswa_panel(self):
    mahasiswa_widget = MahasiswaWindow()
    mahasiswa_widget.select_data()
    self.centralwidget = mahasiswa_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def mahasiswa_on(self):
    mahasiswa_widget = MahasiswaWindow()
    mahasiswa_widget.select_data()
    self.centralwidget = mahasiswa_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

# Matakuliah
def matakuliah_panel(self):
    matakuliah_widget = MatakuliahWindow()
    matakuliah_widget.select_data()
    self.centralwidget = matakuliah_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def matakuliah_on(self):
    matakuliah_widget = MatakuliahWindow()
    matakuliah_widget.select_data()
    self.centralwidget = matakuliah_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

# Prodi
def prodi_panel(self):
    prodi_widget = ProdiWindow()
    prodi_widget.select_data()
    self.centralwidget = prodi_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def prodi_on(self):
    prodi_widget = ProdiWindow()
    prodi_widget.select_data()
    self.centralwidget = prodi_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

# krs full version (admin)
def krs_panel(self):
    krs_widget = KrsWindow()
    self.centralwidget = krs_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def krs_on(self):
    krs_widget = KrsWindow()
    self.centralwidget = krs_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

# input krs
def input_krs_panel(self):
    input_krs_widget = InputKrsWindow()
    self.centralwidget = input_krs_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def input_krs_on(self):
    input_krs_widget = InputKrsWindow()
    self.centralwidget = input_krs_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

# edit krs
def edit_krs_panel(self):
    edit_krs_widget = EditKrsWindow()
    self.centralwidget = edit_krs_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def edit_krs_on(self):
    edit_krs_widget = EditKrsWindow()
    self.centralwidget = edit_krs_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

# edit users
def users_panel(self):
    users_widget = UsersWindow()
    self.centralwidget = users_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def users_on(self):
    users_widget = UsersWindow()
    self.centralwidget = users_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

# edit profile
def profile_panel(self):
    profile_widget = ProfileWindow()
    self.centralwidget = profile_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def profile_on(self):
    profile_widget = ProfileWindow()
    self.centralwidget = profile_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()
