from maya import cmds as cmds

from rigtools.ext import joint


def jointsOnSelectionConn():
    """
    jointsOnSelection UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    joint.jointsOnSelection(sel)


def parentHirarchyConn():
    """
    parentHierarchy UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    joint.parentHirarchy(sel)


def zeroOutConn():
    """
    zeroOut UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    joint.zeroOut(sel)


def selectAllConn():
    """
    selectAll UI connections.
    :return: ui connections
    """
    joint.selectAll()


def orientChainConn(aimAxis, objectUpAxis):
    """
    orientChain UI connections.
    :return: ui connection
    """
    # rtMainUI = rigToolsUI.Ui_mainWindow()
    # rtMainUI.aimX_rb.isChecked()
    # aimAxis = str()
    # objectUpAxis = str()
    aimValue = list()
    objValue = list()
    # radio checks.
    # if Ui_mainWindow.aimX_rb.isChecked():
    #     aimAxis = 'X'
    # if Ui_mainWindow.aimY_rb.isChecked():
    #     aimAxis = 'Y'
    # if Ui_mainWindow.aimZ_rb.isChecked():
    #     aimAxis = 'Z'
    # if Ui_mainWindow.aimObX_rb.isChecked():
    #     objectUpAxis = 'X'
    # if Ui_mainWindow.aimObY_rb.isChecked():
    #     objectUpAxis = 'Y'
    # if Ui_mainWindow.aimObZ_rb.isChecked():
    #     objectUpAxis = 'Z'
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

    joint.orientChain([1,0,0], [0,0,1])

    # sel = cmds.ls(sl=True, type='joint')
    #
    # joint.orientChain(aimValue, objValue)


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
    joint.aimConstraint(aimValue, objValue, sel)


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
    joint.aimConstraintParent(aimValue, objValue, sel)


def noneOrientConn():
    """
    noneOrient UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    joint.noneOrient(sel)


def multiPointConstraintConn():
    """
    mutiPointConstraint UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
    joint.multiPointConstraint(cbVal, sel)


def multiOrientConstraintConn():
    """
    multiOrientConstraint UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
    joint.multiOrientConstraint(cbVal, sel)


def multiParentConstraintConn():
    """
    multiParentConstraint UI connections.
    :return: ui connection
    """
    sel = cmds.ls(sl=True)
    cbVal = cmds.checkBox('maintainOffset_cb', q=True, v=True)
    joint.multiParentConstraint(cbVal, sel)
