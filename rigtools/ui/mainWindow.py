import os

import maya.OpenMayaUI as omui
import maya.cmds as cmds
from PySide import QtGui
from shiboken import wrapInstance

from rigtools.ext import gen
from rigtools.ext import selection
from rigtools.ext import skin
from rigtools.ui import rigTools_ui
from rigtools.ui import ui_fill
from rigtools.ui.utilsUI import jointConn
from rigtools.utils import fk

reload(gen)
reload(skin)
reload(ui_fill)
reload(selection)
reload(fk)
reload(jointConn)

root_dir = os.path.dirname(__file__)
uiFile = os.path.join(root_dir, 'rigTools_ui.ui')
skinUIFile = os.path.join(root_dir, 'skinCopy_ui.ui')
shiftMeshConnUIFile = os.path.join(root_dir, 'shiftInpOutConn_ui.ui')
aspIkOriChangeUIFile = os.path.join(root_dir, 'aspIKOriChange_ui.ui')


def maya_main_window():
    """
    This is to get the maya window QT pointer.
    :return:
    :rtype:
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)


class RigToolsWindow(QtGui.QMainWindow, rigTools_ui.Ui_mainWindow):
    def __init__(self, prnt=None):
        super(RigToolsWindow, self).__init__(prnt)
        self.setupUi(self)
        self.undoStack = QtGui.QUndoStack(self)
        self.connections()

    def connections(self):
        self.jointSel_btn.clicked.connect(jointConn.jointsOnSelectionConn)
        self.parent_btn.clicked.connect(jointConn.parentHirarchyConn)
        self.Zero_Out_btn.clicked.connect(jointConn.zeroOutConn)
        self.Select_All_btn.clicked.connect(jointConn.selectAllConn)
        # self.orient_chain_btn.clicked.connect(self.aa)
        self.aim_constraint_btn.clicked.connect(jointConn.aimConstraintConn)
        self.aim_constraint_parent_btn.clicked.connect(jointConn.aimConstraintParentConn)
        self.none_Orient_btn.clicked.connect(jointConn.noneOrientConn)
        self.point_constraint_btn.clicked.connect(jointConn.multiPointConstraintConn)
        self.orient_constraint_btn.clicked.connect(jointConn.multiOrientConstraintConn)
        self.parent_constraint_btn.clicked.connect(jointConn.multiParentConstraintConn)
        # self.FK_btn.clicked.connect(fkchainConn)
        self.Find_Duplicates_btn.clicked.connect(gen.findDuplicates)
        # self.select_Influence_object_btn.clicked.connect(selectInfluenceObjConn)
        # self.copySkinOnMultipleObject_btn.clicked.connect(windowCopySkin)
        # self.ShiftShapeConnections_btn.clicked.connect(windowShiftMeshConnections)
        # self.IK_Orient_btn.clicked.connect(aspToolsUiConn.aspIkOriChangeWindowConn)

        # self.Hide_Extra_Joints_btn.clicked.connect(aspToolsUiConn.changeDrawStyleOfExtraJointsConn)


show = RigToolsWindow(maya_main_window())


def fkchainConn():
    """
    fkchain UI connections.
    :return: ui connection
    """
    # get axis from ui
    axis = list()
    if cmds.radioButton('ctlAxis_X_rb', q=True, sl=True):
        axis = [1, 0, 0]
    if cmds.radioButton('ctlAxis_Y_rb', q=True, sl=True):
        axis = [0, 1, 0]
    if cmds.radioButton('ctlAxis_Z_rb', q=True, sl=True):
        axis = [0, 0, 1]
    fk.fkchain(axis)


def fkProxyConn():
    """
    fkProxy UI connections.
    :return: ui connection
    """
    # get axis from ui
    axis = list()
    if cmds.radioButton('ctlAxis_X_rb', q=True, sl=True):
        axis = [1, 0, 0]
    if cmds.radioButton('ctlAxis_Y_rb', q=True, sl=True):
        axis = [0, 1, 0]
    if cmds.radioButton('ctlAxis_Z_rb', q=True, sl=True):
        axis = [0, 0, 1]
    fk.fkProxy(axis)


def selectInfluenceObjConn():
    """
    getInfluenceJoint UI Connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    if sel:
        infObj = skin.getInfluenceJoint(sel)
        cmds.select(infObj, r=True)
        print('%s influence objects is selected..' % len(infObj)),
    else:
        cmds.warning('your selection is empty')


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


def shiftInputOutputConnectionsConn():
    """
    shiftInputOutputConnections UI connections.
    :return: ui connection
    """
    sourceInp = cmds.textField('srcInp_LE', q=True, tx=True)
    sourceOut = cmds.textField('srcOut_LE', q=True, tx=True)
    destInp = cmds.textField('destInp_LE', q=True, tx=True)
    destOut = cmds.textField('destOut_LE', q=True, tx=True)
    skin.shiftInputOutputConnections(sourceInp, sourceOut, destInp, destOut)


def createNewShapeBtnConn():
    """
    createNewShapeBtn UI connections.
    :return: ui connection
    """
    newShapeName = cmds.textField('newShpName_LE', q=True, tx=True)
    parent = selection.getSelection()
    gen.createAndParentNewShape(parent[0], newShapeName)


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


def copySkinOnMultiObjectsConn():
    """
    copySkinOnMultiObjects UI Connections.
    :return: ui connection
    """
    source = cmds.textField('sourceMesh_LE', q=True, tx=True)
    target = cmds.textField('destMesh_LE', q=True, tx=True)
    skin.copySkinOnMultiObjects(source, [target])


def skinAndCopySkinConn():
    """
    copySkinOnMultiObjects UI Connections.
    :return: ui connection
    """
    source = cmds.textField('sourceMesh_LE', q=True, tx=True)
    target = cmds.textField('destMesh_LE', q=True, tx=True)
    skin.skinAndCopySkin([source], target)

# ----------------------------------------------------------------------------
