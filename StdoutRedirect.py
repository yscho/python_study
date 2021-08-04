#ref https://4uwingnet.tistory.com/9
import sys

from PyQt5.QtCore import pyqtSignal, QObject, QEventLoop
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic.properties import QtGui

class SystemCmdUi:
    print("test systmeui")

class StdoutRedirect(QObject):
    printOccur = pyqtSignal(str, str, name="print")

    def __init__(self, *param):
        QObject.__init__(self, None)
        self.daemon = True
        self.sysstdout = sys.stdout.write
        self.sysstderr = sys.stderr.write

    def stop(self):
        sys.stdout.write = self.sysstdout
        sys.stderr.write = self.sysstderr

    def start(self):
        sys.stdout.write = self.write
        sys.stderr.write = lambda msg: self.write(msg, color="red")

    def write(self, s, color="black"):
        sys.stdout.flush()
        self.printOccur.emit(s, color)

'''
class ConsoleView(QWidget, sys):
    def __init__(self, parent=None):
        super(ConsoleView, self).__init__(parent)
        self.setupUi(self)

        # member variable
        self._stdout = StdoutRedirect()
        self._stdout.start()
        self._stdout.printOccur.connect(lambda x: self._append_text(x))

    def _append_text(self, msg):
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.textBrowser.insertPlainText(msg)
        # refresh textedit show, refer) https://doc.qt.io/qt-5/qeventloop.html#ProcessEventsFlag-enum
        QApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
'''