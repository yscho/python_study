from PyQt5.Qt import QFileSystemModel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QHeaderView
from PyQt5.QtGui import QFont


class Hwlist_check:
    full = "FULL"
    core = "CORE"

    def __init__(self, Dialog):
        self.combobox_1 = QtWidgets.QComboBox(Dialog)
        self.combobox_1.setGeometry(QtCore.QRect(30, 460, 290, 40))
        font = QFont('Times', 20)
        font.setBold(True)
        font.setFamily("Agency FB")
        self.combobox_1.setFont(font)
        self.combobox_1.addItem(self.full)  # FULL
        self.combobox_1.addItem(self.core)  # CORE
        self.combobox_1.setCurrentIndex(0)


class Secure_check:
    secure = "SECURE"
    nonsecure = "NONSECURE"

    def __init__(self, Dialog):
        self.combobox_sec = QtWidgets.QComboBox(Dialog)
        self.combobox_sec.setGeometry(QtCore.QRect(30, 420, 290, 40))
        #self.combobox_sec.stateChanged.connect(self.check_sec)
        font = QFont('Times', 20)
        font.setBold(True)
        font.setFamily("Agency FB")
        self.combobox_sec.setFont(font)
        self.combobox_sec.addItem(self.secure)  # secure
        self.combobox_sec.addItem(self.nonsecure)  # nonsecure
        self.combobox_sec.setCurrentIndex(0)
