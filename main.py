import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtUiTools import QUiLoader
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

    def start(self):
        incremented_total = self.lcdNumber.intValue() + 1
        self.lcdNumber.display(incremented_total)
        #self.motor.start_motor()

    def stop(self):
        self.motor.emergency_stop()

    def initialize(self):
        """Initializes a Deburr Controller instance which establishes a
        connection with the motor controller"""
        try:
            self.deburr_controller = DeburrController()
        except serial.SerialException as error:
            msg_box = QMessageBox()
            msg_box.setText(error.__str__())
            msg_box.exec_()

    

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    window.initialize()
    app.exec_()
    