import maya.cmds as cmds

from rigtools.utils import joint
from rigtools.ext import gen
from rigtools.ext import selection
from rigtools.utils import constraint
from rigtools import undoChunkOpen


def jointsOnSelectionConn():
    """
    jointsOnSelection UI connections.
    :return: ui connection
    """
    with undoChunkOpen.UndoChunkOpen('jointsOnSelection'):
        sel = cmds.ls(sl=True)
        joint.jointsOnSelection(sel)


def noneOrientConn():
    """
    noneOrient UI connections.
    :return: ui connection
    """
    with undoChunkOpen.UndoChunkOpen('jointsOnSelection'):
        sel = cmds.ls(sl=True)
        joint.noneOrient(sel)


def parentHirarchyConn():
    """
    parentHierarchy UI connections.
    :return: ui connection
    """
    with undoChunkOpen.UndoChunkOpen('jointsOnSelection'):
        sel = cmds.ls(sl=True)
        gen.parentHirarchy(sel)


def zeroOutConn():
    """
    zeroOut UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    gen.zeroOut(sel)


def selectAllConn():
    """
    selectAll UI connections.
    :return: ui connections
    """
    selection.selectAll()


def orientChainConn():
    """
    orientChain UI connections.
    :return: ui connection
    """
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


def aimConstraintConn():
    """
    aimConstraint UI connections.
    :return: ui connection
    """
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
    sel = cmds.ls(sl=True)
    cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
    constraint.multiPointConstraint(cbVal, sel)


def multiOrientConstraintConn():
    """
    multiOrientConstraint UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
    constraint.multiOrientConstraint(cbVal, sel)


def multiParentConstraintConn():
    """
    multiParentConstraint UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
    constraint.multiParentConstraint(cbVal, sel)
