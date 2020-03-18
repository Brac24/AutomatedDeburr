import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget

class Form(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        start_button = QPushButton("Start")
        hlayout = QHBoxLayout()
        hlayout.addWidget(start_button)
        widget = QWidget()
        widget.setLayout(hlayout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication()
    main_window = Form()
    main_window.show()
    app.exec_()