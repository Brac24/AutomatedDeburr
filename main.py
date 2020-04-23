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
import serial
from Worker import Worker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.deburr_controller = None
        validator = QIntValidator(1, 200, self) # Validator for the operation time input. Only allow values 1 to 100 seconds
        self.operation_time_entry.setValidator(validator)
        self.current_elapsed_time = 0
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_elapsed_time)
        self.max_deburr_time = 0
        self.thread_pool = QThreadPool()

    def update_elapsed_time(self):
        if (self.current_elapsed_time - 1) == 0:
            self.timer.stop()
            time.sleep(.5) #sleep for half second before turning dc motors off to synchonize a bit with rotary
            self.deburr_controller.stop_deburr()
            incremented_total = self.lcdNumber.intValue() + 1            # Increment number of deburred pieces
            self.lcdNumber.display(incremented_total)                    # Update displays of deburred pieces
            self.start_button.setDisabled(False)
        
        self.current_elapsed_time = self.current_elapsed_time - 1
        self.elapsed_time_label.setText(f'{self.current_elapsed_time}')

    def reset_elapsed_time(self):
        self.current_elapsed_time = self.max_deburr_time
        self.elapsed_time_label.setText(f'{self.current_elapsed_time}')

    def start(self):
        #t = threading.Thread(target=self.deburr_controller.start_deburr, args=(self.operation_time_entry.text(),))
        worker = Worker(self.deburr_controller.start_deburr, self.operation_time_entry.text())
        if self.operation_time_entry.text() == "":
            error = "Please Enter an Operation Time"
        else:
            #error = self.deburr_controller.start_deburr(self.operation_time_entry.text())
            error = None

       # if error is None:
        self.max_deburr_time = int(self.operation_time_entry.text()) # Set total operation time
        self.reset_elapsed_time()                                    # Reset time at start of operation
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
        self.deburr_controller.e_stop()


    def initialize(self):
        """Initializes a Deburr Controller instance which establishes a
        connection with the motor controller"""
        self.deburr_controller = DeburrController()
        error = self.deburr_controller.startup()
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
