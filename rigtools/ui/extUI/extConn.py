from maya import cmds as cmds

from rigtools.ext import gen, selection, skin
from rigtools import undoChunkOpen


# --------------------------------------------------------------
# -------------------------- gen -------------------------------
# --------------------------------------------------------------
def findDuplicatesConn():
    """
    findDuplicates UI connections.
    :return: ui connection
    """
    with undoChunkOpen.UndoChunkOpen('jointsOnSelection'):
        gen.findDuplicates()


def createNewShapeBtnConn():
    """
    createNewShapeBtn UI connections.
    :return: ui connection
    """
    with undoChunkOpen.UndoChunkOpen('createNewShape'):
        newShapeName = cmds.textField('newShpName_LE', q=True, tx=True)
        parent = selection.getSelection()
        gen.createAndParentNewShape(parent[0], newShapeName)


def zeroOutConn():
    """
    zeroOut UI connections.
    :return: ui connection
    """
    with undoChunkOpen.UndoChunkOpen('zeroOut'):
        sel = cmds.ls(sl=True)
        gen.zeroOut(sel)


def parentHirarchyConn():
    """
    parentHierarchy UI connections.
    :return: ui connection
    """
    with undoChunkOpen.UndoChunkOpen('parentHirarchy'):
        sel = cmds.ls(sl=True)
        gen.parentHirarchy(sel)


# --------------------------------------------------------------
# ----------------------- selection ----------------------------
# --------------------------------------------------------------
def selectAllConn():
    """
    selectAll UI connections.
    :return: ui connections
    """
    with undoChunkOpen.UndoChunkOpen('selectAll'):
        selection.selectAll()


# --------------------------------------------------------------
# ------------------------- skin -------------------------------
# --------------------------------------------------------------
def selectInfluenceObjConn():
    """
    getInfluenceJoint UI Connections.
    :return: ui connection
    """
    with undoChunkOpen.UndoChunkOpen('selectInfluenceObj'):
        sel = cmds.ls(sl=True)
        if sel:
            infObj = skin.getInfluenceJoint(sel)
            cmds.select(infObj, r=True)
            print('%s influence objects is selected..' % len(infObj)),
        else:
            cmds.warning('your selection is empty')


def copySkinOnMultiObjectsConn():
    """
    copySkinOnMultiObjects UI Connections.
    :return: ui connection
    """
    with undoChunkOpen.UndoChunkOpen('copySkinOnMultiObjects'):
        source = cmds.textField('sourceMesh_LE', q=True, tx=True)
        target = cmds.textField('destMesh_LE', q=True, tx=True)
        skin.copySkinOnMultiObjects(source, [target])


def skinAndCopySkinConn():
    """
    copySkinOnMultiObjects UI Connections.
    :return: ui connection
    """
    with undoChunkOpen.UndoChunkOpen('skinAndCopySkin'):
        source = cmds.textField('sourceMesh_LE', q=True, tx=True)
        target = cmds.textField('destMesh_LE', q=True, tx=True)
        skin.skinAndCopySkin([source], target)


def shiftInputOutputConnectionsConn():
    """
    shiftInputOutputConnections UI connections.
    :return: ui connection
    """
    with undoChunkOpen.UndoChunkOpen('shiftInputOutputConnections'):
        sourceInp = cmds.textField('srcInp_LE', q=True, tx=True)
        sourceOut = cmds.textField('srcOut_LE', q=True, tx=True)
        destInp = cmds.textField('destInp_LE', q=True, tx=True)
        destOut = cmds.textField('destOut_LE', q=True, tx=True)
        skin.shiftInputOutputConnections(sourceInp, sourceOut, destInp, destOut)
