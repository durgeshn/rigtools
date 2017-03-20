import pymel.core as pm
import maya.OpenMaya as om


def findDuplicates():
    """@brief Check for nodes with duplicate name and add them to errors node.
    """
    duplicateNames = list()
    for node in pm.ls():
        if "|" in str(node):
            if not node.isInstanced():
                duplicateNames.append(str(node))
            else:
                if len(pm.ls(node)) > 1:
                    duplicateNames.append(str(node))
    if not duplicateNames:
        print ('No duplicates in scene...'),
        return True
    pm.select(cl=True)
    if pm.objExists('SET_duplicate_names'):
        pm.delete('SET_duplicate_names')
    pm.sets(n='SET_duplicate_names', em=True).union(duplicateNames)
    print ('%s duplicate objects has been found and put in the "SET_duplicate_names".' % len(duplicateNames)),
    return False


def createAndParentNewShape(parent, newShapeName):
    """
    create new shape from parent add it on as shape parent with parent.
    :param parent: string
    :param newShapeName: string
    :return: newShape
    """
    parent = pm.PyNode(parent)
    dupParent = pm.duplicate(parent, rr=True)
    newShape = dupParent[0].getShapes()[0]
    newShape.rename(newShapeName)
    pm.parent(newShape, parent, r=True, s=True)
    pm.delete(dupParent)
    newShape.setIntermediateObject(False)
    return str(newShape)


def identifyInpOutShapes(source):
    """
    identify shapes who has inputs and output connection.
    :param source: string
    :return: inputShape and output shape.
    """
    # get inputs from source.
    source = pm.PyNode(source)
    inpShape = str()
    outShape = str()
    sourceShapes = source.getShapes()
    if len(sourceShapes) == 2:
        for each in sourceShapes:
            if each.isIntermediateObject():
                outShape = each
            else:
                inpShape = each
    else:
        pm.warning('source mesh has more than two shapes or only one shape...')
        return False
    return str(inpShape), str(outShape)


def distanceCompareBetweenTwoObjects(objA, objB):
    """
    get xform of two objects and minus its and get return.
    :param objA: string
    :param objB: string
    :return: positions (x,y,z)
    """
    obj1 = pm.PyNode(objA)
    obj2 = pm.PyNode(objB)
    obj1Pos = pm.xform(obj1, q=True, ws=True, t=True)
    obj2Pos = pm.xform(obj2, q=True, ws=True, t=True)

    posA = obj1Pos[0] - obj2Pos[0]
    posB = obj1Pos[1] - obj2Pos[1]
    posC = obj1Pos[2] - obj2Pos[2]
    return posA, posB, posC


def getLength(valX, valY, valZ):
    """
    get length
    :param valX: float
    :param valY: float
    :param valZ: float
    :return: length (float)
    """
    distance = om.MVector(valX, valY, valZ)
    return distance.length()
