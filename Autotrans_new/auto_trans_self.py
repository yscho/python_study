import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import clipboard
import autotranse

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
#form_class = uic.loadUiType("./Autotrans_up.ui")[0]
from Autotrans_upui import Ui_MainWindow

#화면을 띄우는데 사용되는 Class 선언
# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow):
    def __init__(self) :
        QMainWindow.__init__(self)
        # UI 선언
        main_ui = Ui_MainWindow()
        # UI 준비
        main_ui.setupUi(self)
        main_ui.plainTextEdit.setPlainText(clipboard.paste())
        autotranse.trans_from_clipbd()
        main_ui.plainTextEdit_2.setPlainText(clipboard.paste())
        # 화면을 보여준다.
        self.show()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()