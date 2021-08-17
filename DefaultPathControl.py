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
        #self.treeView_explorer.doubleClicked()

        self.bt_path_search = QtWidgets.QPushButton(Dialog)
        self.bt_path_search.clicked.connect(self.showDialog_Path)

        self.bt_path_open = QtWidgets.QPushButton(Dialog)
        self.bt_path_open.clicked.connect(self.open_path_by_url)

        self.bt_path_save = QtWidgets.QPushButton(Dialog)
        self.bt_path_save.clicked.connect(self.save_path)

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
        self.label.setObjectName("label")

    def save_path(self):
        print("save_path ")
        f = open(self.path_filename, 'w')
        f.write(self.lineEdit_path_txt.text())
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
        fname = QFileDialog.getExistingDirectory(self.bt_path_search, 'Select Directory', 'c:')
        self.qfsmodel_path.setRootPath(fname)
        self.index_root_path = self.qfsmodel_path.index(self.qfsmodel_path.rootPath())
        self.treeView_explorer.setRootIndex(self.index_root_path)
        self.lineEdit_path_txt.setText(fname)

    def open_path_by_url(self):
        urlpath = self.lineEdit_path_txt.text()
        print(urlpath)
        if os.path.exists(urlpath):
            self.qfsmodel_path.setRootPath(urlpath)
            self.index_root_path = self.qfsmodel_path.index(self.qfsmodel_path.rootPath())
            self.treeView_explorer.setRootIndex(self.index_root_path)
        else:
            print("ERR : There is not exist path")

    #@pyqtSlot(QtCore.QModelIndex)
    def on_treeView_explorer_clicked(self, index):
        indexItem = self.qfsmodel_path.index(index.row(), 0, index.parent())
        filePath = self.qfsmodel_path.filePath(indexItem)
        self.lineEdit_path_txt.setText(filePath)
