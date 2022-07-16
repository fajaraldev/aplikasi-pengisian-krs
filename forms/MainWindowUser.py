import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence as QKSec
from GUI.RibbonButton import RibbonButton
from GUI.Icons import get_icon
from GUI.RibbonTextbox import RibbonTextbox
from GUI.RibbonWidget import *
from panel.Panel import *

class MainWindowUser(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.resize(1280, 800)
        self.setWindowTitle("Main Window User")
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("icon"))
        child_panels(self)

        # actions
        self._input_krs_action = self.add_action("Input KRS", "ico_krs", "Input KRS", True, self.on_input_krs)
        self._edit_krs_action = self.add_action("Edit KRS", "ico_krs", "Edit KRS", True, self.on_edit_krs)

        self._profile_action = self.add_action("Profile", "profile", "Profile", True, self.on_profile)
        self._logout_action = self.add_action("Logout", "logout", "Logout", True, self.on_logout)
        self._zoom_action = self.add_action("Search", "search", "Search", True, self.on_zoom)
        self._about_action = self.add_action("About", "about", "About", True, self.on_about)
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
        file_pane.add_ribbon_widget(RibbonButton(self, self._input_krs_action, True))

        edit_panel = home_tab.add_ribbon_pane("Edit")
        edit_panel.add_ribbon_widget(RibbonButton(self, self._edit_krs_action, True))

        view_panel = home_tab.add_ribbon_pane("View")
        view_panel.add_ribbon_widget(RibbonButton(self, self._zoom_action, True))
        home_tab.add_spacer()

        about_tab = self._ribbon.add_ribbon_tab("About")
        info_panel = about_tab.add_ribbon_pane("Info")
        info_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        info_panel.add_ribbon_widget(RibbonButton(self, self._license_action, True))

        settings_tab = self._ribbon.add_ribbon_tab("Settings")
        info_panel = settings_tab.add_ribbon_pane("View")
        info_panel.add_ribbon_widget(RibbonButton(self, self._profile_action, True))
        info_panel.add_ribbon_widget(RibbonButton(self, self._logout_action, True))
        etc_panel = settings_tab.add_ribbon_pane("Etc")
        etc_panel.add_ribbon_widget(RibbonButton(self, self._exit_action, True))

    # Ribbon Button Functions
    def closeEvent(self, close_event):
        pass

    def on_save_to_excel(self):
        pass

    def on_profile(self):
        profile_on(self)

    def on_input_krs(self):
        input_krs_on(self)

    def on_edit_krs(self):
        edit_krs_on(self)

    def on_zoom(self):
        pass

    def on_about(self):
        text = "PostgreSQL CRUD | Aplikasi Input Data KRS\n"
        text += "Copyright © 2022 UMC"
        QMessageBox().about(self, "About App", text)

    def on_license(self):
        text = """
Copyright 2022 UMC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

        QMessageBox().about(self, "License App", text)

    def on_logout(self):
        text = "PostgreSQL CRUD App\n"
        text += "Copyright © 2022 Freddy Wicaksono"
        QMessageBox().about(self, "About App", text)

    def app_exit(self):
      sys.exit()
