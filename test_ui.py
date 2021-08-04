# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from subprocess import run, PIPE, Popen

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeView, QFileDialog
from PyQt5.Qt import QFileSystemModel
from PyQt5.QtCore import pyqtSlot, QEventLoop, pyqtSignal, QObject
import os
import shutil
import StdoutRedirect
import DefaultPathControl

class Ui_Dialog(object):

    src_path_filename = "./src_default_path.bin"
    tar_path_filename = "./tar_default_path.bin"


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(723, 900)

        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(610, 30, 91, 21))
        self.checkBox.setObjectName("checkBox")

        self.oPathControl_AndroTar = DefaultPathControl.CexplorerPathControl(self.tar_path_filename, Dialog)
        self.oPathControl_AndroTar.lineEdit_path_txt.setGeometry(QtCore.QRect(30, 350, 291, 31))
        self.oPathControl_AndroTar.treeView_explorer.setGeometry(QtCore.QRect(30, 140, 291, 192))
        self.oPathControl_AndroTar.bt_path_search.setGeometry(QtCore.QRect(30, 100, 120, 23))
        self.oPathControl_AndroTar.bt_path_search.setObjectName("bt_androPath")
        self.oPathControl_AndroTar.bt_path_open.setGeometry(QtCore.QRect(220, 385, 100, 20))
        self.oPathControl_AndroTar.bt_path_open.setObjectName("bt_movepaht_and")
        self.oPathControl_AndroTar.bt_path_save.setGeometry(QtCore.QRect(110, 385, 100, 20))
        self.oPathControl_AndroTar.bt_path_save.setObjectName("bt_savepath_and")

        self.oPathControl_FacosSrc = DefaultPathControl.CexplorerPathControl(self.src_path_filename, Dialog)
        self.oPathControl_FacosSrc.lineEdit_path_txt.setGeometry(QtCore.QRect(370, 350, 291, 31))
        self.oPathControl_FacosSrc.treeView_explorer.setGeometry(QtCore.QRect(370, 140, 291, 192))
        self.oPathControl_FacosSrc.bt_path_search.setGeometry(QtCore.QRect(370, 100, 120, 23))
        self.oPathControl_FacosSrc.bt_path_search.setObjectName("bt_facosPath")
        self.oPathControl_FacosSrc.bt_path_open.setGeometry(QtCore.QRect(560, 385, 100, 20))
        self.oPathControl_FacosSrc.bt_path_open.setObjectName("bt_movepaht_fac")
        self.oPathControl_FacosSrc.bt_path_save.setGeometry(QtCore.QRect(450, 385, 100, 20))
        self.oPathControl_FacosSrc.bt_path_save.setObjectName("bt_savepath_fac")

        self.oPathControl_AndroTar.label.setGeometry(QtCore.QRect(500, 90, 141, 31))
        self.oPathControl_FacosSrc.label.setGeometry(QtCore.QRect(170, 90, 141, 31))

#button Setting
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 60, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        # ------------------TEMP BT--------------------------------------------------
        self.bt_temp1 = QtWidgets.QPushButton(Dialog)
        self.bt_temp1.setGeometry(QtCore.QRect(30, 470, 113, 20))
        self.bt_temp1.setObjectName("temp_bt1")
        self.bt_temp1.clicked.connect(self.file_cp)

        self.bt_temp2 = QtWidgets.QPushButton(Dialog)
        self.bt_temp2.setGeometry(QtCore.QRect(30, 490, 113, 20))
        self.bt_temp2.setObjectName("temp_bt2")

        self.bt_temp3 = QtWidgets.QPushButton(Dialog)
        self.bt_temp3.setGeometry(QtCore.QRect(30, 510, 113, 20))
        self.bt_temp3.setObjectName("temp_bt3")

        self.bt_temp4 = QtWidgets.QPushButton(Dialog)
        self.bt_temp4.setGeometry(QtCore.QRect(30, 530, 113, 20))
        self.bt_temp4.setObjectName("temp_bt4")
        self.bt_temp4.clicked.connect(self.run_os_system)

        # Text Browser setting

        self.systemBrowser = QtWidgets.QTextBrowser(Dialog)
        self.systemBrowser.setGeometry(QtCore.QRect(30, 580, 640, 240))
        self.systemBrowser.setObjectName("systemBrowser")
        self.systemBrowser.setText("test Default=================")

        #--------------------------------------------------------------------
        self._stdout = StdoutRedirect.StdoutRedirect(self)
        self._stdout.start()
        self._stdout.printOccur.connect(lambda x: self._append_text(x))


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "Secure"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.oPathControl_AndroTar.bt_path_search.setText(_translate("Dialog", "And_path_open"))
        self.oPathControl_FacosSrc.bt_path_search.setText(_translate("Dialog", "FacOS_path_open"))

        self.oPathControl_AndroTar.bt_path_open.setText(_translate("Dialog", "open_Android"))
        self.oPathControl_FacosSrc.bt_path_open.setText(_translate("Dialog", "open_Facos"))
        self.oPathControl_AndroTar.bt_path_save.setText(_translate("Dialog", "Save_Tar_path"))
        self.oPathControl_FacosSrc.bt_path_save.setText(_translate("Dialog", "Save_Src_path"))

        self.bt_temp1.setText(_translate("Dialog", "file cp test"))
        self.bt_temp2.setText(_translate("Dialog", "temp2"))
        self.bt_temp3.setText(_translate("Dialog", "temp3"))
        self.bt_temp4.setText(_translate("Dialog", "calc cmd test"))
        self.oPathControl_AndroTar.label.setText(_translate("Dialog", "FactoryOS PATH View"))
        self.oPathControl_FacosSrc.label.setText(_translate("Dialog", "Android PATH View"))

    def file_cp(self):
        print("test file copy")
        src_path = self.lineEdit_facos_src.text()
        print(src_path)
        src_path = src_path + '\*'
        target_path = self.lineEdit_andro_tar.text()
        print(src_path)
        print(target_path)
        #self.copyDirTree(src_path,target_path)
        temp_cmd = 'copy '+ src_path + ' ' + target_path
        #shutil.move(src_path, target_path)
        #shutil.copy(src_path, target_path)
        os.system(temp_cmd)

        #check_Facview = self.treeView_Facos.state()
        #print(check_Facview)

    def copyDirTree(root_src_dir, root_dst_dir):
        """
        Copy directory tree. Overwrites also read only files.
        :param root_src_dir: source directory
        :param root_dst_dir:  destination directory
        """

        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    try:
                        os.remove(dst_file)
                    except PermissionError as exc:
                        os.chmod(dst_file, stat.S_IWUSR)
                        os.remove(dst_file)

                shutil.copy(src_file, dst_dir)

    def run_os_system(self):
        import subprocess

        bat_cmd = "dir"
        p = subprocess.Popen(bat_cmd, stdout=subprocess.PIPE, shell=True)
        result = p.stdout.read()
        result2 = result.decode('euc-kr')

        print(result2)

        #os.system(bat_cmd)

    def _append_text(self, msg):
        self.systemBrowser.moveCursor(QtGui.QTextCursor.End)
        #self.systemBrowser.toPlainText().encode('utf-8')
        self.systemBrowser.insertPlainText(msg)
        # refresh textedit show, refer) https://doc.qt.io/qt-5/qeventloop.html#ProcessEventsFlag-enum
        QApplication.processEvents(QEventLoop.ExcludeUserInputEvents)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    #test_ui_im.retranslateUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
