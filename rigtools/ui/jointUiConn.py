from maya import cmds as cmds

import rigtools.ext.gen
import rigtools.utils.constraint
import rigtools.utils.joint
from rigtools.ext import joint


def jointsOnSelectionConn():
    """
    jointsOnSelection UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    rigtools.utils.joint.jointsOnSelection(sel)


def parentHirarchyConn():
    """
    parentHierarchy UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    rigtools.ext.gen.parentHirarchy(sel)


def zeroOutConn():
    """
    zeroOut UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    rigtools.ext.gen.zeroOut(sel)


def selectAllConn():
    """
    selectAll UI connections.
    :return: ui connections
    """
    rigtools.ext.gen.selectAll()


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
    rigtools.utils.joint.orientChain(aimValue, objValue, sel)


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
    rigtools.utils.constraint.aimConstraint(aimValue, objValue, sel)


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
    rigtools.utils.constraint.aimConstraintParent(aimValue, objValue, sel)


def noneOrientConn():
    """
    noneOrient UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    rigtools.utils.joint.noneOrient(sel)


def multiPointConstraintConn():
    """
    mutiPointConstraint UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
    rigtools.utils.constraint.multiPointConstraint(cbVal, sel)


def multiOrientConstraintConn():
    """
    multiOrientConstraint UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
    rigtools.utils.constraint.multiOrientConstraint(cbVal, sel)


def multiParentConstraintConn():
    """
    multiParentConstraint UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
    rigtools.utils.constraint.multiParentConstraint(cbVal, sel)
