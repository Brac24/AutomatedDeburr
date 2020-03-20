import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow
from MotorController import MotorController
from DeburrController import DeburrController

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.controller = DeburrController()
        #self.motor = MotorController()


    def start(self):
        incremented_total = self.lcdNumber.intValue() + 1
        self.lcdNumber.display(incremented_total)
        #self.motor.start_motor()

    def stop(self):
        self.motor.emergency_stop()
    

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()