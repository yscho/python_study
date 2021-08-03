import os
from PyQt5.Qt import QFileSystemModel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class CexplorerPathControl:

    def __init__(self, path_filename, Dialog):
        self.path_filename = path_filename
        self.default_path = ""
        self.temp_path = "test"
        self.load_path()

        self.lineEdit_path_txt = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_path_txt.setObjectName("textBrowser")
        self.lineEdit_path_txt.setText(self.temp_path)

        self.qfsmodel_path = QFileSystemModel()
        self.qfsmodel_path.setRootPath(self.load_path())
        self.index_root_path = self.qfsmodel_path.index(self.qfsmodel_path.rootPath())

        self.treeView_explorer = QtWidgets.QTreeView(Dialog)
        self.treeView_explorer.setModel(self.qfsmodel_path)
        self.treeView_explorer.setObjectName("treeView_control")
        self.treeView_explorer.setRootIndex(self.index_root_path)
        self.treeView_explorer.clicked.connect(self.on_treeView_explorer_clicked)

        self.bt_path_select = QtWidgets.QPushButton(Dialog)
        self.bt_path_select.clicked.connect(self.showDialog_Path)

    def save_path(self, full_path):
        print("save_path ")
        f = open(self.path_filename, 'w')
        f.write(full_path)
        f.close()

    def load_path(self):
        if os.path.isfile(self.path_filename):
            f = open(self.path_filename, 'r')
            self.temp_path = f.readline()
            print(self.temp_path)
            f.close()
        else:
            self.temp_path = self.default_path
        return self.temp_path

    def showDialog_Path(self):
        fname = QFileDialog.getExistingDirectory(self.bt_path_select, 'Select Directory', 'c:')
        self.qfsmodel_path.setRootPath(fname)
        self.index_root_path = self.qfsmodel_path.index(self.qfsmodel_path.rootPath())
        self.treeView_explorer.setRootIndex(self.index_root_path)
        self.lineEdit_path_txt.setText(fname)

    def open_path_url_and(self):
        urlpath = self.lineEdit_path_txt.text()
        print(urlpath)
        self.qfsmodel_path.setRootPath(urlpath)
        self.index_root_path = self.qfsmodel_path.index(self.qfsmodel_path.rootPath())
        self.treeView_explorer.setRootIndex(self.index_root_path)

    #@pyqtSlot(QtCore.QModelIndex)
    def on_treeView_explorer_clicked(self, index):
        indexItem = self.qfsmodel_path.index(index.row(), 0, index.parent())
        filePath = self.qfsmodel_path.filePath(indexItem)
        self.lineEdit_path_txt.setText(filePath)
