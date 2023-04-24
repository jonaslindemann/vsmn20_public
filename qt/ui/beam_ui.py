# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:44:29 2016

@author: lindemann
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import beam_model as bm

class BeamWindow(QWidget):
    """Main window class"""

    def __init__(self):
        """BeamWindow constructor"""
        super().__init__()

        # Create model instance

        self.beam = bm.BeamSimplySupported()

        # Initialise user interface

        self.init_gui()

        # Update controls with values from model instance

        self.update_controls()
        self.update_text_edit()

    def init_gui(self):
        """Initialise user interface"""

        self.resize(500, 400)
        self.move(50, 50)
        self.setWindowTitle("Beam calculator")

        # Create controls

        self.a_label = QLabel("a (m)")
        self.a_edit = QLineEdit()

        self.b_label = QLabel("b (m)")
        self.b_edit = QLineEdit()

        self.P_label = QLabel("P (N)")
        self.P_edit = QLineEdit()

        self.E_label = QLabel("E (Pa)")
        self.E_edit = QLineEdit()

        self.I_label = QLabel("I (Pa)")
        self.I_edit = QLineEdit()

        self.text_edit = QTextEdit("")
        self.text_edit.setFont(QFont("Courier", 6))

        # Create layout

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.a_label, 0, 0)
        self.grid.addWidget(self.a_edit,  0, 1)
        self.grid.addItem(QSpacerItem(300, 0), 0, 2)

        self.grid.addWidget(self.b_label, 1, 0)
        self.grid.addWidget(self.b_edit,  1, 1)

        self.grid.addWidget(self.P_label, 2, 0)
        self.grid.addWidget(self.P_edit,  2, 1)

        self.grid.addWidget(self.E_label, 3, 0)
        self.grid.addWidget(self.E_edit,  3, 1)

        self.grid.addWidget(self.I_label, 4, 0)
        self.grid.addWidget(self.I_edit,  4, 1)

        self.grid.addWidget(self.text_edit, 5, 0, 2, 0)

        self.grid.setContentsMargins(8, 8, 8, 8)

        self.grid.setHorizontalSpacing(8)
        self.grid.setVerticalSpacing(8)

        self.setLayout(self.grid)

        # Connect events

        self.a_edit.editingFinished.connect(self.on_editing_finished)
        self.b_edit.editingFinished.connect(self.on_editing_finished)
        self.P_edit.editingFinished.connect(self.on_editing_finished)
        self.E_edit.editingFinished.connect(self.on_editing_finished)
        self.I_edit.editingFinished.connect(self.on_editing_finished)

    def update_controls(self):
        """Update controls with model values"""
        
        print("update_controls")

        self.a_edit.setText(str(self.beam.a))
        self.b_edit.setText(str(self.beam.b))
        self.P_edit.setText(str(self.beam.P))
        self.E_edit.setText(str(self.beam.E))
        self.I_edit.setText(str(self.beam.I))

    def update_text_edit(self):
        """Update text controls"""

        self.text_edit.clear()
        self.text_edit.append('{:>10}  {:>10}  {:>10}  {:>10}'.format("x (m)", "v (m)", "V (N)", "M (Nm)"))

        x = 0.0
        dx = 0.1

        while x < self.beam.L + dx:
            self.text_edit.append('{:10.5}  {:10.5}  {:10.5}  {:10.5}'.format(
                x, self.beam.v(x), self.beam.V(x), self.beam.M(x)))
            x += dx

        self.text_edit.moveCursor(QTextCursor.Start)

    def update_model(self):
        """Update model with values from controls"""

        print("update_model")

        self.beam.a = self.a_edit.text()
        self.beam.b = self.b_edit.text()
        self.beam.P = self.P_edit.text()
        self.beam.E = self.E_edit.text()
        self.beam.I = self.I_edit.text()

    def on_editing_finished(self):
        """Update """

        # Make sure values in controls reflect the model .
        # If users enters invalid values they have to be removed.

        # Get current values from controls

        self.update_model()

        # Fill text box with beam section values.

        self.update_text_edit()

        self.update_controls() 


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = BeamWindow()
    window.show()

    sys.exit(app.exec_())
