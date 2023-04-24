# -*- coding: utf-8 -*-

import sys

from qtpy.QtWidgets import *

if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = QWidget()
    widget.show()

    sys.exit(app.exec_())
