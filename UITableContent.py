from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout, QTabWidget
from UICategoryTabs import TeamTab, TripsTab, DocumentsTab, RanksTab, SkillsTab


class UITableContent(QWidget):
    def __init__(self, parent=None):
        super(UITableContent, self).__init__(parent)

        self.layout = QGridLayout()
        """self.manageButton = QPushButton('Dodaj', self)
        self.layout.addWidget(self.manageButton, 1, 0)"""

        self.tabs = QTabWidget()
        self.tabs.addTab(TeamTab(), "Członkowie")
        self.tabs.addTab(TripsTab(), "Wyjazdy")
        self.tabs.addTab(DocumentsTab(), "Rozkazy")
        self.tabs.addTab(SkillsTab(), "Sprawności")
        self.tabs.addTab(RanksTab(), "Sprawności")
        self.layout.addWidget(self.tabs, 0, 0, 1, 3)






