import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget
from PySide2.QtUiTools import QUiLoader


# This is an example of simply loading the .ui file and being able to access ui elements
# by simply referencing the name of the ui element

#Disadvantages
# 1. Will not get code completion and checking when accessing these elements because the
#    element is not visible to the application until run time.
if __name__ == "__main__":
    app = QApplication()
    loader = QUiLoader()
    ui = loader.load('test.ui')
    my_widget = ui.cancelButton # access of ui element.
    ui.show()
    app.exec_()