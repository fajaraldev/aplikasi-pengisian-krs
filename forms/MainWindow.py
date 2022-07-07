import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence as QKSec
from GUI.RibbonButton import RibbonButton
from GUI.Icons import get_icon
from GUI.RibbonTextbox import RibbonTextbox
from GUI.RibbonWidget import *
from panel.Panel import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.resize(1280, 800)
        self.setWindowTitle("Main Window")
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("icon"))
        child_panels(self)

        # -------------      actions       -----------------
        self._matakuliah_action = self.add_action("Matakuliah", "ico_matakuliah", "Data Matakuliah", True, self.on_matakuliah)
        self._mahasiswa_action = self.add_action("Mahasiswa", "ico_mahasiswa", "Data Mahasiswa", True, self.on_mahasiswa)
        self._prodi_action = self.add_action("Prodi", "ico_prodi", "Data Prodi", True, self.on_prodi)
        self._krs_action = self.add_action("KRS", "ico_krs", "Data KRS", True, self.on_krs)

        self._zoom_action = self.add_action("Search", "zoom", "Search", True, self.on_zoom)
        self._about_action = self.add_action("About", "about", "About QupyRibbon", True, self.on_about)
        self._license_action = self.add_action("License", "license", "Licence for this software", True, self.on_license)
        self._exit_action = self.add_action("Exit", "exit", "Exit", True, self.app_exit)

        # Ribbon
        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)
        self.init_ribbon()

    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action

    def init_ribbon(self):
        home_tab = self._ribbon.add_ribbon_tab("Home")
        file_pane = home_tab.add_ribbon_pane("File")
        file_pane.add_ribbon_widget(RibbonButton(self, self._mahasiswa_action, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self._matakuliah_action, True))

        edit_panel = home_tab.add_ribbon_pane("Edit")
        edit_panel.add_ribbon_widget(RibbonButton(self, self._prodi_action, True))
        edit_panel.add_ribbon_widget(RibbonButton(self, self._krs_action, True))


        view_panel = home_tab.add_ribbon_pane("View")
        view_panel.add_ribbon_widget(RibbonButton(self, self._zoom_action, True))
        view_panel.add_ribbon_widget(RibbonButton(self, self._exit_action, True))
        home_tab.add_spacer()

        about_tab = self._ribbon.add_ribbon_tab("About")
        info_panel = about_tab.add_ribbon_pane("Info")
        info_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        info_panel.add_ribbon_widget(RibbonButton(self, self._license_action, True))

       # -------------      Ribbon Button Functions      -----------------

    def closeEvent(self, close_event):
        pass

    def on_save_to_excel(self):
        pass

    def on_matakuliah(self):
        matakuliah_on(self)

    def on_mahasiswa(self):
        mahasiswa_on(self)

    def on_prodi(self):
        prodi_on(self)

    def on_krs(self):
        input_krs_on(self)

    def on_zoom(self):
        pass

    def on_license(self):
        pass

    def on_about(self):
        text = "PostgreSQL CRUD App\n"
        text += "Copyright © 2022 Freddy Wicaksono"
        QMessageBox().about(self, "About App", text)

    def app_exit(self):
      sys.exit()
