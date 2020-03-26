import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget, QLabel
from PySide2.QtCore import QTimer
import time

# In this application we are laying out the GUI using code

# Disadvantages
# 1. GUI would not be portable (i.e. will have to redo GUI if rewritten in C++)
class Form(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        start_button = QPushButton("Start")
        hlayout = QHBoxLayout()
        hlayout.addWidget(start_button)
        widget = QWidget()
        widget.setLayout(hlayout)
        self.setCentralWidget(widget)
        self.label = QLabel(self)
        self.label.setText("0")
        self.current_time = 0
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_elapsed_time)
        self.timer.start()
        

    def update_elapsed_time(self):
        self.current_time = self.current_time + 1
        self.label.setText(f'{self.current_time}')

    def do_something(self):
        hi = 1
        time.sleep(3)

if __name__ == "__main__":
    app = QApplication()
    main_window = Form()
    main_window.show()
    main_window.do_something()
    app.exec_()