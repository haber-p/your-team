from PyQt5.QtWidgets import QMainWindow, QMenu
from UITableContent import UITableContent
from databaseWindow import DatabaseWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(350, 50, 700, 750)
        self.setFixedSize(1100, 950)
        self.setWindowTitle("Twoja drużyna")
        self._startUIStart()
        self._createMenuBar()

    def _createMenuBar(self):
        menuBar = self.menuBar()
        databaseMenu = menuBar.addMenu("&Database")
        settings = databaseMenu.addAction("Settings")
        settings.triggered.connect(self.databaseWindow)

    def _startUIStart(self):
        self.Window = UITableContent(self)
        self.Window.setLayout(self.Window.layout)
        self.setCentralWidget(self.Window)

    def databaseWindow(self):
        widget = DatabaseWindow()
        widget.exec_()



