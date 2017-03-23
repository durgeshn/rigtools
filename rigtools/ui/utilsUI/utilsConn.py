import maya.cmds as cmds

from rigtools import maya_utils
from rigtools.utils import fk
from rigtools.utils import constraint
from rigtools.utils import joint


# --------------------------------------------------------------
# ------------------- constraint -------------------------------
# --------------------------------------------------------------
def aimConstraintConn():
    """
    aimConstraint UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('aimConstraint'):
        aimAxis = str()
        objectUpAxis = str()
        aimValue = list()
        objValue = list()
        # radio checks.
        if cmds.radioButton('aimX_rb', q=True, sl=True):
            aimAxis = 'X'
        if cmds.radioButton('aimY_rb', q=True, sl=True):
            aimAxis = 'Y'
        if cmds.radioButton('aimZ_rb', q=True, sl=True):
            aimAxis = 'Z'
        if cmds.radioButton('aimObX_rb', q=True, sl=True):
            objectUpAxis = 'X'
        if cmds.radioButton('aimObY_rb', q=True, sl=True):
            objectUpAxis = 'Y'
        if cmds.radioButton('aimObZ_rb', q=True, sl=True):
            objectUpAxis = 'Z'
        if aimAxis == 'X':
            aimValue = [1, 0, 0]
        if aimAxis == 'Y':
            aimValue = [0, 1, 0]
        if aimAxis == 'Z':
            aimValue = [0, 0, 1]
        if objectUpAxis == 'X':
            objValue = [1, 0, 0]
        if objectUpAxis == 'Y':
            objValue = [0, 1, 0]
        if objectUpAxis == 'Z':
            objValue = [0, 0, 1]
        sel = cmds.ls(sl=True)
        constraint.aimConstraint(aimValue, objValue, sel)


def aimConstraintParentConn():
    """
    aimConstraintParent UI connections.
    :return: connection
    """
    with maya_utils.UndoChunkOpen('aimConstraintParent'):
        aimAxis = str()
        objectUpAxis = str()
        aimValue = list()
        objValue = list()
        # radio checks.
        if cmds.radioButton('aimX_rb', q=True, sl=True):
            aimAxis = 'X'
        if cmds.radioButton('aimY_rb', q=True, sl=True):
            aimAxis = 'Y'
        if cmds.radioButton('aimZ_rb', q=True, sl=True):
            aimAxis = 'Z'
        if cmds.radioButton('aimObX_rb', q=True, sl=True):
            objectUpAxis = 'X'
        if cmds.radioButton('aimObY_rb', q=True, sl=True):
            objectUpAxis = 'Y'
        if cmds.radioButton('aimObZ_rb', q=True, sl=True):
            objectUpAxis = 'Z'
        if aimAxis == 'X':
            aimValue = [1, 0, 0]
        if aimAxis == 'Y':
            aimValue = [0, 1, 0]
        if aimAxis == 'Z':
            aimValue = [0, 0, 1]
        if objectUpAxis == 'X':
            objValue = [1, 0, 0]
        if objectUpAxis == 'Y':
            objValue = [0, 1, 0]
        if objectUpAxis == 'Z':
            objValue = [0, 0, 1]
        sel = cmds.ls(sl=True, type='joint')
        constraint.aimConstraintParent(aimValue, objValue, sel)


def multiPointConstraintConn():
    """
    mutiPointConstraint UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('multiPointConstraint'):
        sel = cmds.ls(sl=True)
        cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
        constraint.multiPointConstraint(cbVal, sel)


def multiOrientConstraintConn():
    """
    multiOrientConstraint UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('multiOrientConstraint'):
        sel = cmds.ls(sl=True)
        cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
        constraint.multiOrientConstraint(cbVal, sel)


def multiParentConstraintConn():
    """
    multiParentConstraint UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('multiParentConstraint'):
        sel = cmds.ls(sl=True)
        cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
        constraint.multiParentConstraint(cbVal, sel)


# --------------------------------------------------------------
# -------------------------- fk --------------------------------
# --------------------------------------------------------------
def fkchainConn():
    """
    fkchain UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('multiParentConstraint'):
        # get axis from ui
        axis = list()
        if cmds.radioButton('ctlAxis_X_rb', q=True, sl=True):
            axis = [1, 0, 0]
        if cmds.radioButton('ctlAxis_Y_rb', q=True, sl=True):
            axis = [0, 1, 0]
        if cmds.radioButton('ctlAxis_Z_rb', q=True, sl=True):
            axis = [0, 0, 1]
        fk.fkchain(axis)


# --------------------------------------------------------------
# ------------------------ joint -------------------------------
# --------------------------------------------------------------
def jointsOnSelectionConn():
    """
    jointsOnSelection UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('jointsOnSelection'):
        sel = cmds.ls(sl=True)
        joint.jointsOnSelection(sel)


def noneOrientConn():
    """
    noneOrient UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('noneOrient'):
        sel = cmds.ls(sl=True)
        joint.noneOrient(sel)


def orientChainConn():
    """
    orientChain UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('orient chain'):
        aimAxis = str()
        objectUpAxis = str()
        aimValue = list()
        objValue = list()
        # radio checks.
        if cmds.radioButton('aimX_rb', q=True, sl=True):
            aimAxis = 'X'
        if cmds.radioButton('aimY_rb', q=True, sl=True):
            aimAxis = 'Y'
        if cmds.radioButton('aimZ_rb', q=True, sl=True):
            aimAxis = 'Z'
        if cmds.radioButton('aimObX_rb', q=True, sl=True):
            objectUpAxis = 'X'
        if cmds.radioButton('aimObY_rb', q=True, sl=True):
            objectUpAxis = 'Y'
        if cmds.radioButton('aimObZ_rb', q=True, sl=True):
            objectUpAxis = 'Z'
        if aimAxis == 'X':
            aimValue = [1, 0, 0]
        if aimAxis == 'Y':
            aimValue = [0, 1, 0]
        if aimAxis == 'Z':
            aimValue = [0, 0, 1]
        if objectUpAxis == 'X':
            objValue = [1, 0, 0]
        if objectUpAxis == 'Y':
            objValue = [0, 1, 0]
        if objectUpAxis == 'Z':
            objValue = [0, 0, 1]
        sel = cmds.ls(sl=True, type='joint')
        joint.orientChain(aimValue, objValue, sel)
