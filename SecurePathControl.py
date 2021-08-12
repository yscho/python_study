import os
from PyQt5.Qt import QFileSystemModel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QHeaderView


class CexplorerPathControl:

    def __init__(self, path_filename, Dialog):
        self.path_filename = path_filename
        self.default_path = path_filename
        self.temp_path = "test"
        self.load_path()

        self.lineEdit_path_txt = QtWidgets.QLabel(Dialog)#QLineEdit(Dialog)
        self.lineEdit_path_txt.setText(self.temp_path)

        self.qfsmodel_path = QFileSystemModel()
        self.qfsmodel_path.setRootPath(self.load_path())
        self.index_root_path = self.qfsmodel_path.index(self.qfsmodel_path.rootPath())

        self.treeView_explorer = QtWidgets.QTreeView(Dialog)
        self.treeView_explorer.header().sectionResizeMode(QHeaderView.ResizeToContents)
        #self.treeView_explorer.setEnabled(False)

        self.treeView_explorer.setModel(self.qfsmodel_path)
        self.treeView_explorer.setObjectName("treeView_control")
        self.treeView_explorer.setRootIndex(self.index_root_path)


        self.label = QtWidgets.QLabel(Dialog)
        #self.label.setGeometry(QtCore.QRect(500, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.label_disable = QtWidgets.QLabel(Dialog)
        #self.label_disable.setGeometry(QtCore.QRect(400, 450, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(45)
        font.setBold(True)
        self.label_disable.setFont(font)
        self.label_disable.setText("NO COPY")
        self.label_disable.setStyleSheet("Color : red")
        self.label_disable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_disable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_disable.setTextFormat(QtCore.Qt.AutoText)
        self.label_disable.setScaledContents(False)
        self.label_disable.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disable.setVisible(False)


    def load_path(self):
        self.temp_path = self.default_path
        return self.temp_path


    def open_path_by_url(self, text):
        urlpath = text
        self.qfsmodel_path.setRootPath(urlpath)
        self.index_root_path = self.qfsmodel_path.index(self.qfsmodel_path.rootPath())
        self.treeView_explorer.setRootIndex(self.index_root_path)
        self.lineEdit_path_txt.setText(urlpath)

    #@pyqtSlot(QtCore.QModelIndex)
    def on_treeView_explorer_clicked(self, index):
        indexItem = self.qfsmodel_path.index(index.row(), 0, index.parent())
        filePath = self.qfsmodel_path.filePath(indexItem)
        self.lineEdit_path_txt.setText(filePath)
