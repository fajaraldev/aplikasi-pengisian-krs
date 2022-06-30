from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmMahasiswa import MahasiswaWindow
from forms.frmMatakuliah import MatakuliahWindow
from forms.frmDosen import DosenWindow
from forms.frmAgenda import AgendaWindow

dock = QtWidgets.QDockWidget()

def child_panels(self):
    matakuliah_panel(self)
    mahasiswa_panel(self)
    dosen_panel(self)
    agenda_panel(self)

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

# Dosen
def dosen_panel(self):
    dosen_widget = DosenWindow()
    dosen_widget.select_data()
    self.centralwidget = dosen_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def dosen_on(self):
    dosen_widget = DosenWindow()
    dosen_widget.select_data()
    self.centralwidget = dosen_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

# Agenda
def agenda_panel(self):
    agenda_widget = AgendaWindow()
    agenda_widget.select_data()
    self.centralwidget = agenda_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def agenda_on(self):
    agenda_widget = AgendaWindow()
    agenda_widget.select_data()
    self.centralwidget = agenda_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()
