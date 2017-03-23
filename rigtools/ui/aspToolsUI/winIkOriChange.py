import os

from PySide import QtGui

from rigtools import undoChunkOpen
from rigtools.ui import mainWindow
from rigtools.ui.aspToolsUI import ui_aspIKOriChange
from rigtools.ui import ui_fill
from rigtools.aspTools import tools

reload(ui_fill)

aspTools_dir = os.path.dirname(__file__)


class IkOrientUIConn(QtGui.QMainWindow, ui_aspIKOriChange.Ui_aspIKOriChangeWindow):
    def __init__(self, prnt=None):
        super(IkOrientUIConn, self).__init__(prnt)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.aspIkOriJntLd_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.aspIkOriJnt_LE))
        self.aspIkOriCtlLd_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.aspIkOriCtl_LE))
        self.aspIkOriSet_btn.clicked.connect(self.asIKCtlOriChangeConn)

    def asIKCtlOriChangeConn(self):
        with undoChunkOpen.UndoChunkOpen('Ik Orient Change'):
            jnt = self.aspIkOriJnt_LE.text()
            ctl = self.aspIkOriCtl_LE.text()
            tools.asIKCtlOriChange(jnt, ctl)


def main():
    winClass = IkOrientUIConn(mainWindow.maya_main_window())
    return winClass.show()
