import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtGui import QValidator, QIntValidator
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QTimer
from ui_mainwindow import Ui_MainWindow
from MotorController import MotorController
from DeburrController import DeburrController
import serial


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.deburr_controller = None
        validator = QIntValidator(1, 100, self) # Validator for the operation time input. Only allow values 1 to 100 seconds
        self.operation_time_entry.setValidator(validator)
        self.current_elapsed_time = 0
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_elapsed_time)
        self.max_deburr_time = 0

    def update_elapsed_time(self):
        if self.current_elapsed_time == (self.max_deburr_time - 1):
            self.timer.stop()
            self.deburr_controller.stop_deburr()
            incremented_total = self.lcdNumber.intValue() + 1            # Increment number of deburred pieces
            self.lcdNumber.display(incremented_total)                    # Update displays of deburred pieces
        
        self.current_elapsed_time = self.current_elapsed_time - 1
        self.elapsed_time_label.setText(f'{self.current_elapsed_time}')

    def reset_elapsed_time(self):
        self.current_elapsed_time = self.max_deburr_time
        self.elapsed_time_label.setText(f'{self.current_elapsed_time}')

    def start(self):
        if self.operation_time_entry.text() == "":
            error = "Please Enter an Operation Time"
        else:
            error = self.deburr_controller.start_deburr(self.operation_time_entry.text())

        if error is None:
            self.reset_elapsed_time()                                    # Reset time at start of operation
            self.max_deburr_time = int(self.operation_time_entry.text()) # Set total operation time
            self.timer.start()                                           # Start timer
        else:
            self.display_error(error)

    def display_error(self, msg):
        msg_box = QMessageBox()
        msg_box.setText(msg)
        msg_box.exec_()

    def stop(self):
        print('stop')

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
