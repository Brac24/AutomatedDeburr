import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget
from PySide2.QtUiTools import QUiLoader



if __name__ == "__main__":
    app = QApplication()
    loader = QUiLoader()
    ui = loader.load('test.ui')
    my_widget = ui.cancelButton
    ui.show()
    app.exec_()