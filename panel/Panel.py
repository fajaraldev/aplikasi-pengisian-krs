from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmMahasiswa import MahasiswaWindow
from forms.frmMatakuliah import MatakuliahWindow
from forms.frmProdi import ProdiWindow
from forms.frmInputKrs import InputKrsWindow

dock = QtWidgets.QDockWidget()

def child_panels(self):
    matakuliah_panel(self)
    mahasiswa_panel(self)
    prodi_panel(self)
    input_krs_panel(self)

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

# input krs
def input_krs_panel(self):
    input_krs_widget = InputKrsWindow()
    input_krs_widget.select_data()
    self.centralwidget = input_krs_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def input_krs_on(self):
    input_krs_widget = InputKrsWindow()
    input_krs_widget.select_data()
    self.centralwidget = input_krs_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()
