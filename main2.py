import sys
import threading
import time
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtGui import QValidator, QIntValidator
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QTimer, QThreadPool
from ui_mainwindow import Ui_MainWindow
from MotorController import MotorController
from DeburrController import DeburrController
from MainControl import MainControl
import serial
from Worker import Worker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.main_controller = None
        validator = QIntValidator(1, 200, self) # Validator for the operation time input. Only allow values 1 to 100 seconds
        self.operation_time_entry.setValidator(validator)
        self.current_elapsed_time = 0
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_elapsed_time)
        self.max_deburr_time = 0
        self.thread_pool = QThreadPool()

    def update_elapsed_time(self):
        time_left = self.main_controller.update_elapsed()
        self.elapsed_time_label.setText(f'{time_left}')

        if (self.main_controller.is_done()):
            self.timer.stop()
            self.start_button.setDisabled(False)
            parts_deburred = self.main_controller.stop()
            self.lcdNumber.display(parts_deburred)                    # Update displays of deburred pieces
              

    def reset_elapsed_time(self):
        self.current_elapsed_time = self.max_deburr_time
        

    def start(self):
        if self.operation_time_entry.text() == "":
            error = "Please Enter an Operation Time"
        else: error = None

       # if error is None:
        max_deburr_time = int(self.operation_time_entry.text()) # Set total operation time
        worker = Worker(self.main_controller.start, max_deburr_time)
        self.elapsed_time_label.setText(f'{max_deburr_time}') # Reset time label at start of operation
        self.thread_pool.start(worker)#self.deburr_controller.start_deburr(self.operation_time_entry.text())
        self.timer.start()                                           # Start timer
        #t.join()
        
        if error is not None:
            self.display_error(error)
        else:
            self.start_button.setDisabled(True)

    def display_error(self, msg):
        msg_box = QMessageBox()
        msg_box.setText(msg)
        msg_box.exec_()

    def stop(self):
        if self.main_controller.is_in_progress():
            self.timer.stop()
            time_left = self.main_controller.e_stop() # Tiny G is reset here
            # User must wait for Tiny G to reset.
            # We need a way to know when the system is ready to go
            # Start button should be disabled until the system is ready
            self.start_button.setDisabled(False) # for now we will enable start button right away
            self.elapsed_time_label.setText(f'{time_left}')
        else:
            self.display_error('System is not running')


    def initialize(self):
        """Initializes a Deburr Controller instance which establishes a
        connection with the motor controller"""
        self.main_controller = MainControl()
        error = self.main_controller.startup()
        if error is not None:
            msg_box = QMessageBox()
            msg_box.setText(error.__str__())
            msg_box.exec_()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    window.initialize()
    app.exec_()
