#This shows an example of how to use a generated python class to access UI elements in a .ui file
#The generated file is ui_mainwindow.py and was generated using pyside2-uic command
#Full command was pyside2-uic test.ui -o ui_mainwindow.py
#where test.ui is the .ui file created from Qt Designer
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget
from PySide2.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.cancelButton.setText('Hey')

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()