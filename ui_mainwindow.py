# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui',
# licensing of 'main_ui.ui' applies.
#
# Created: Wed Mar 25 14:36:36 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 200, 381, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_button = QtWidgets.QPushButton(self.layoutWidget)
        self.start_button.setAutoFillBackground(True)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_2.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(self.layoutWidget)
        self.stop_button.setAutoFillBackground(True)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_2.addWidget(self.stop_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 360, 137, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.elapsed_time_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.elapsed_time_label.setFont(font)
        self.elapsed_time_label.setObjectName("elapsed_time_label")
        self.horizontalLayout_3.addWidget(self.elapsed_time_label)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(190, 140, 301, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setMaximumSize(QtCore.QSize(270, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.operation_time_entry = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operation_time_entry.sizePolicy().hasHeightForWidth())
        self.operation_time_entry.setSizePolicy(sizePolicy)
        self.operation_time_entry.setMinimumSize(QtCore.QSize(20, 0))
        self.operation_time_entry.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.operation_time_entry.setFont(font)
        self.operation_time_entry.setMaxLength(3)
        self.operation_time_entry.setObjectName("operation_time_entry")
        self.horizontalLayout_4.addWidget(self.operation_time_entry)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Parts Deburred:", None, -1))
        self.start_button.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))
        self.stop_button.setText(QtWidgets.QApplication.translate("MainWindow", "Stop", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Elapsed Time:", None, -1))
        self.elapsed_time_label.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Operation Run Time (seconds):", None, -1))

