import sys
from PyQt5.QtWidgets import QApplication
from mainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    #ShpViewerCtrl(view=view)
    sys.exit(app.exec())