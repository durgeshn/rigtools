import os

import maya.cmds as cmds

from rigtools.ext import joint
from rigtools.ext import gen
from rigtools.ext import selection
from rigtools.ext import skin
from rigtools.ui import ui_fill
from rigtools.utils import fk

reload(joint)
reload(gen)
reload(skin)
reload(ui_fill)
reload(selection)
reload(fk)

root_dir = os.path.dirname(__file__)
uiFile = os.path.join(root_dir, 'rigTools_ui.ui')
skinUIFile = os.path.join(root_dir, 'skinCopy_ui.ui')
shiftMeshConnUIFile = os.path.join(root_dir, 'shiftInpOutConn_ui.ui')
aspIkOriChangeUIFile = os.path.join(root_dir, 'aspIKOriChange_ui.ui')


def mainWindow():
    """
    rigtools main window button connections.
    :return: ui
    """
    # open Window.
    if cmds.window('mainWindow', exists=True):
        cmds.deleteUI('mainWindow')
    rigToolUI = cmds.loadUI(f=uiFile)
    cmds.showWindow(rigToolUI)
    # joint button connections.
    cmds.button('jointSel_btn', e=True, c='from rigtools.ui import jointUiConn; jointUiConn.jointsOnSelectionConn()')
    cmds.button('parent_btn', e=True, c='from rigtools.ui import jointUiConn; jointUiConn.parentHirarchyConn()')
    cmds.button('Zero_Out_btn', e=True, c='from rigtools.ui import jointUiConn; jointUiConn.zeroOutConn()')
    cmds.button('Select_All_btn', e=True, c='from rigtools.ui import jointUiConn; jointUiConn.selectAllConn()')
    cmds.button('orient_chain_btn', e=True, c='from rigtools.ui import jointUiConn; jointUiConn.orientChainConn()')
    cmds.button('aim_constraint_btn', e=True, c='from rigtools.ui import jointUiConn; jointUiConn.aimConstraintConn()')
    cmds.button('aim_constraint_parent_btn', e=True,
                c='from rigtools.ui import jointUiConn; jointUiConn.aimConstraintParentConn()')
    cmds.button('none_Orient_btn', e=True, c='from rigtools.ui import jointUiConn; jointUiConn.noneOrientConn()')
    cmds.button('point_constraint_btn', e=True,
                c='from rigtools.ui import jointUiConn; jointUiConn.multiPointConstraintConn()')
    cmds.button('orient_constraint_btn', e=True,
                c='from rigtools.ui import jointUiConn; jointUiConn.multiOrientConstraintConn()')
    cmds.button('parent_constraint_btn', e=True,
                c='from rigtools.ui import jointUiConn; jointUiConn.multiParentConstraintConn()')
    # controller button connections.
    cmds.button('FK_btn', e=True, c='mainWindow.fkchainConn()')
    # gen button connections.
    cmds.button('Find_Duplicates_btn', e=True, c='from rigtools.utils import gen;gen.findDuplicates()')
    # skin button connections.
    cmds.button('select_Influence_object_btn', e=True, c='mainWindow.selectInfluenceObjConn()')
    cmds.button('copySkinOnMultipleObject_btn', e=True, c='mainWindow.windowCopySkin()')
    cmds.button('ShiftShapeConnections_btn', e=True, c='mainWindow.windowShiftMeshConnections()')
    # asp tool button connections.
    cmds.button('IK_Orient_btn', e=True,
                c='from rigtools.ui import aspToolsUiConn;aspToolsUiConn.aspIkOriChangeWindowConn()')
    cmds.button('Hide_Extra_Joints_btn', e=True,
                c='from rigtools.ui import aspToolsUiConn;aspToolsUiConn.changeDrawStyleOfExtraJointsConn()')


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
    rigtools.utils.fk.fkchain(axis)


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
    rigtools.utils.fk.fkProxy(axis)


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
