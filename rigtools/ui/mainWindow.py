import os

from PySide import QtGui

from rigtools.ext import gen
from rigtools.ui import rigTools_ui
from rigtools.ui.aspToolsUI import winIkOriChange
from rigtools.ui.extUI import extConn
from rigtools.ui.utilsUI import utilsConn
from rigtools import maya_utils

reload(gen)
reload(rigTools_ui)
reload(winIkOriChange)
reload(utilsConn)
reload(extConn)
reload(maya_utils)

root_dir = os.path.dirname(__file__)
skinUIFile = os.path.join(root_dir, 'skinCopy_ui.ui')
shiftMeshConnUIFile = os.path.join(root_dir, 'shiftInpOutConn_ui.ui')


class RigToolsUIConn(QtGui.QMainWindow, rigTools_ui.Ui_mainWindow):
    def __init__(self, prnt=None):
        super(RigToolsUIConn, self).__init__(prnt)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.jointSel_btn.clicked.connect(utilsConn.jointsOnSelectionConn)
        self.parent_btn.clicked.connect(extConn.parentHirarchyConn)
        self.Zero_Out_btn.clicked.connect(extConn.zeroOutConn)
        self.Select_All_btn.clicked.connect(extConn.selectAllConn)
        # self.orient_chain_btn.clicked.connect(self.aa)
        self.aim_constraint_btn.clicked.connect(utilsConn.aimConstraintConn)
        self.aim_constraint_parent_btn.clicked.connect(utilsConn.aimConstraintParentConn)
        self.none_Orient_btn.clicked.connect(utilsConn.noneOrientConn)
        self.point_constraint_btn.clicked.connect(utilsConn.multiPointConstraintConn)
        self.orient_constraint_btn.clicked.connect(utilsConn.multiOrientConstraintConn)
        self.parent_constraint_btn.clicked.connect(utilsConn.multiParentConstraintConn)
        # self.FK_btn.clicked.connect(fkchainConn)
        self.Find_Duplicates_btn.clicked.connect(gen.findDuplicates)
        # self.select_Influence_object_btn.clicked.connect(selectInfluenceObjConn)
        # self.copySkinOnMultipleObject_btn.clicked.connect(windowCopySkin)
        # self.ShiftShapeConnections_btn.clicked.connect(windowShiftMeshConnections)
        self.IK_Orient_btn.clicked.connect(winIkOriChange.main)
        # self.Hide_Extra_Joints_btn.clicked.connect(aspToolsUiConn.changeDrawStyleOfExtraJointsConn)


def main():
    winClass = RigToolsUIConn(maya_utils.maya_main_window())
    return winClass.show()
