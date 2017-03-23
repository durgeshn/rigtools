import os

import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide import QtGui
from shiboken import wrapInstance

from rigtools.ext import gen
from rigtools.ui import rigTools_ui
from rigtools.ui.utilsUI import utilsConn
from rigtools.ui.extUI import extConn
from rigtools.ui.aspToolsUI import winIkOriChange

reload(gen)
reload(rigTools_ui)
reload(winIkOriChange)
reload(utilsConn)
reload(extConn)

root_dir = os.path.dirname(__file__)
skinUIFile = os.path.join(root_dir, 'skinCopy_ui.ui')
shiftMeshConnUIFile = os.path.join(root_dir, 'shiftInpOutConn_ui.ui')


def maya_main_window():
    """
    This is to get the maya window QT pointer.
    :return:
    :rtype:
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)


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


show = RigToolsUIConn(maya_main_window())


# ----------------------------------------------------------------------------
# window shift mesh ui connection functions.
# ----------------------------------------------------------------------------
def windowShiftMeshConnections():
    """
    ShiftInpOutConnWindow UI connections.
    :return: ui connection
    """
    if cmds.window('ShiftInpOutConnWindow', exists=True):
        cmds.deleteUI('ShiftInpOutConnWindow')
    shiftMeshConnUI = cmds.loadUI(f=shiftMeshConnUIFile)
    cmds.showWindow(shiftMeshConnUI)
    cmds.button('newShapeCreate_btn', e=True, c='mainWindow.createNewShapeBtnConn()')
    cmds.button('srcInpLd_btn', e=True, c='from rigtools.ui import ui_fill;ui_fill.addInTextField("srcInp_LE")')
    cmds.button('srcOutLd_btn', e=True, c='from rigtools.ui import ui_fill;ui_fill.addInTextField("srcOut_LE")')
    cmds.button('destInpLd_btn', e=True, c='from rigtools.ui import ui_fill;ui_fill.addInTextField("destInp_LE")')
    cmds.button('destOutLd_btn', e=True, c='from rigtools.ui import ui_fill;ui_fill.addInTextField("destOut_LE")')
    cmds.button('shiftConnections_btn', e=True, c='mainWindow.shiftInputOutputConnectionsConn()')


# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# window copy skin and createAndCopySkin ui connection functions.
# ----------------------------------------------------------------------------
def windowCopySkin():
    """
    windowCopySkin UI connections.
    :return: ui connection
    """
    if cmds.window('skinCopyWindow', exists=True):
        cmds.deleteUI('skinCopyWindow')
    copySkinUI = cmds.loadUI(f=skinUIFile)
    cmds.showWindow(copySkinUI)
    cmds.button('sourceMeshLoad_btn', e=True,
                c='from rigtools.ui import ui_fill;ui_fill.addInTextField("sourceMesh_LE")')
    cmds.button('destMeshLoad_btn', e=True, c='from rigtools.ui import ui_fill;ui_fill.addInTextField("destMesh_LE")')
    cmds.button('copySkin_btn', e=True, c='mainWindow.copySkinOnMultiObjectsConn()')
    cmds.button('skin_copySkin_btn', e=True, c='mainWindow.skinAndCopySkinConn()')

# ----------------------------------------------------------------------------
