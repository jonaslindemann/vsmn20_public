# -*- coding: utf-8 -*-

import sys

from qtpy.QtWidgets import QApplication, QWidget, QPushButton
from qtpy.QtCore import QCoreApplication

class MyWindow(QWidget):
    def __init__(self):
        """MyWindow konstruktor"""
        super().__init__()

        # Setup user interface

        self.init_gui()

    def init_gui(self):
        """Initiera gränssnitt"""

        # Create button control

        self.button = QPushButton("Press me", self)
        self.button.setToolTip("I am a button. Please press me")
        self.button.resize(100,50)
        self.button.move(50,50)

        # Window properties

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("MyWidget")

        # Show window

        self.show()

    def on_button_clicked(self):
        """Händelsemetod för signalen clicked"""
        print("Hello")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Skapa vårt MyWindow objekt

    window = MyWindow()

    # Starta händelseloop

    sys.exit(app.exec_())
