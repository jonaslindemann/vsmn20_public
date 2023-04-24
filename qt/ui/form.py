# -*- coding: utf-8 -*-

import sys

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

        uic.loadUi("form8.ui", self)

        self.press_me_button.setText("My button")
        self.press_me_button.clicked.connect(self.on_button_press)
        
    def on_button_press(self):
        print("button pressed")


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
