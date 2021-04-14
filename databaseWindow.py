from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit, QWidget, QPushButton


class DatabaseWindow(QDialog):
    def __init__(self, parent=None):
        super(DatabaseWindow, self).__init__(parent)
        self.setGeometry(350, 50, 300, 250)
        self.setFixedSize(300, 250)
        self.setWindowTitle("Database settings")

        hostLine = QLineEdit()
        databaseLine = QLineEdit()
        userLine = QLineEdit()
        passwordLine = QLineEdit()
        portLine = QLineEdit()

        testBtn = QPushButton("Test")
        acceptBtn = QPushButton("Ok")
        backBtn = QPushButton("Back")

        layout = QGridLayout()
        layout.addWidget(QLabel("host"), 1, 0, 1, 1)
        layout.addWidget(hostLine, 1, 1, 1, 2)
        layout.addWidget(QLabel("database"), 2, 0)
        layout.addWidget(databaseLine, 2, 1, 1, 2)
        layout.addWidget(QLabel("user"), 3, 0)
        layout.addWidget(userLine, 3, 1, 1, 2)
        layout.addWidget(QLabel("password"), 4, 0)
        layout.addWidget(passwordLine, 4, 1, 1, 2)
        layout.addWidget(QLabel("port"), 5, 0)
        layout.addWidget(portLine, 5, 1, 1, 2)
        layout.addWidget(testBtn, 6,0,1,1)
        layout.addWidget(acceptBtn, 6, 1, 1, 1)
        layout.addWidget(backBtn, 6, 2, 1, 1)
        self.setLayout(layout)





