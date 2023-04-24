# -*- coding: utf-8 -*-

import sys, os, subprocess, time

from qtpy.QtWidgets import *
from qtpy.QtCore import *
from qtpy import uic

class ExampleRunner:
    def __init__(self):
        super().__init__()

        self.examples = {}

    def find_examples(self):
        for item in os.listdir():
            if os.path.isfile(item):
                if ".py" in item:
                    self.examples[item] = "Example"

    def run(self, name):
        p = subprocess.Popen(["python", name])

class MainWindow(QMainWindow):
    """Main window class for the Flow application"""

    def __init__(self):
        """Class constructor"""

        super().__init__()

        # Load and show our user interface

        self.init_gui()

        # Find examples:

        self.example_runner = ExampleRunner()
        self.example_runner.find_examples()
        #self.example_runner.run("form.py")

        row = 0
        max_rows = 20
        col = 0

        for example in self.example_runner.examples.keys():
            #label_example = QLabel(example)
            #label_example.setAlignment(Qt.AlignRight)
            button_run = QPushButton(example)
            button_run.clicked.connect(self.on_run_example)
            #button_edit = QPushButton("Edit")
            #button_edit.clicked.connect(self.on_edit_example)
            #self.button_grid.addWidget(label_example, row, col)
            self.button_grid.addWidget(button_run, row, col+1)
            #self.button_grid.addWidget(button_edit, row, col+2)

            if row>max_rows:
                row = 0
                col += 1
            else:
                row += 1

    def init_gui(self):
        """Initialisera gränssnitt"""

        uic.loadUi("example_starter.ui", self)

    def on_run_example(self):
        b = self.sender()
        self.example_runner.run(b.text())

    def on_edit_example(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
