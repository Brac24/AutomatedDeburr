import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.start_button.clicked.connect(self.start)

    def start(self):
        incremented_total = self.lcdNumber.intValue() + 1
        self.lcdNumber.display(incremented_total)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()