#This shows an example of how to use a generated python class to access UI elements in a .ui file
#The generated file is ui_mainwindow.py and was generated using pyside2-uic command
#Full command was: pyside2-uic test.ui -o ui_mainwindow.py
#where test.ui is the .ui file created from Qt Designer

#That command just needs to get run whenever the .ui file changes

# Disadvantages
# 1. Renaming of elements is not automatic so if we change multiple element names in the .ui file
#    we would have to remember which element names changed and change the names in all places
#    where the old element name is referenced. This is easy with the rename tool but can become
#    cumbersome if we don't remember what the old element name was.
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cancelButton.setText('Hey')

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.ui.cancelButton.setText('No') # We can access element from outside by first accessing ui member
    window.show()
    app.exec_()