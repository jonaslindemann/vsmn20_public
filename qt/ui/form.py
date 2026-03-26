# -*- coding: utf-8 -*-

import sys

from qtpy.QtCore import Qt
from qtpy.QtWidgets import *
from qtpy import uic

class MainWindow(QWidget):
    """Main window class for the Flow application"""

    def __init__(self):
        """Class constructor"""

        super().__init__()

        # Load and show our user interface

        self.init_gui()

    def init_gui(self):
        """Initialisera gränssnitt"""

        uic.loadUi("form11.ui", self)

        self.my_button.setText("My button")
        self.my_button.clicked.connect(self.on_button_press)
        
    def on_button_press(self):
        print("button pressed")


if __name__ == '__main__':

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
