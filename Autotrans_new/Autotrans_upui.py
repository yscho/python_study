# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Autotrans_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 421, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.Target_text = QtWidgets.QWidget()
        self.Target_text.setObjectName("Target_text")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.Target_text)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 411, 241))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.Target_text, "")
        self.Trans_result = QtWidgets.QWidget()
        self.Trans_result.setObjectName("Trans_result")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.Trans_result)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 0, 361, 201))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.tabWidget.addTab(self.Trans_result, "")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(130, 370, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Target_text), _translate("MainWindow", "Target_text"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Trans_result), _translate("MainWindow", "Trans_result"))

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())