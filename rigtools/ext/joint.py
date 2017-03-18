import maya.cmds as cmds


def jointsOnSelection(sel=None):
    """
    joints on selected items.
    :param sel: list (joint)
    :return: joint
    """
    if not sel:
        sel = cmds.ls(sl=True, fl=True)
    if not sel:
        cmds.warning('Please select at least one object...')
        return False
    allJoints = list()
    for i in range(len(sel)):
        cmds.select(cl=True)
        pos = cmds.xform(sel[i], q=True, ws=True, t=True)
        rot = cmds.xform(sel[i], q=True, ws=True, ro=True)
        jnt = cmds.joint(p=[pos[0], pos[1], pos[2]])
        cmds.xform(jnt, ws=True, ro=[rot[0], rot[1], rot[2]])
        allJoints.append(jnt)
    cmds.select(allJoints, r=True)


def parentHirarchy(sel=None):
    """
    parent objects using selection order.
    parent selection needs to be in children to parent.
    :param sel: list
    :return: parented chain
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if len(sel) < 2:
        cmds.warning('Please select two or more item...')
    else:
        for i in range(len(sel) - 1):
            cmds.parent(sel[i], sel[i + 1])
        cmds.select(sel[len(sel) - 1])


def zeroOut(sel=None):
    """
    zeroOut all the selected objects.
    :param sel: list
    :return: upper group
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        cmds.warning('Please select at least on object...')
    else:
        for i in range(len(sel)):
            name = sel[i] + 'ZERO'
            if cmds.objExists(name):
                raise RuntimeError('%s is already exist please rename it and run zeroOut again...' % name)
            else:
                grp = cmds.group(em=True, w=True, n=name)
                par = cmds.listRelatives(sel[i], p=True)
                cmds.delete(cmds.parentConstraint(sel[i], grp))
                cmds.parent(sel[i], grp)
                if not par:
                    pass
                else:
                    cmds.parent(grp, par[0])


def selectAll():
    """
    select hierarchy of all selected objects.
    :return: hierarchy
    """
    cmds.select(hi=True)


def orientChain(aimValue, objValue, sel=None):
    """
    select top joint and unparent it,
    then rotate or orient it for object up axis,
    then parent it again and execute script.
    :param sel: list (joint)
    :param aimValue: list ([1,0,0])
    :param objValue: list ([1,0,0])
    :return: orientation
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        cmds.warning('Please select at least on object...')
        return False
    for x in range(len(sel)):
        cmds.select(cl=True)
        allJoints = cmds.ls(sel[x], dag=True)
        if len(allJoints) > 1:
            cmds.parent(allJoints[1:], w=True)
            for i in range(len(allJoints)):
                if i != len(allJoints) - 1:
                    cmds.select(cl=True)
                    # create locator and snap on selection one.
                    loc = cmds.spaceLocator(n='TempLocatorForObjectUpOrientation')
                    cmds.delete(cmds.parentConstraint(allJoints[i], loc[0]))
                    if objValue == [1, 0, 0]:
                        cmds.move(3, 0, 0, loc[0], r=True, os=True, wd=True)
                    if objValue == [0, 1, 0]:
                        cmds.move(0, 3, 0, loc[0], r=True, os=True, wd=True)
                    if objValue == [0, 0, 1]:
                        cmds.move(0, 0, 3, loc[0], r=True, os=True, wd=True)
                    cmds.delete(cmds.aimConstraint(allJoints[i + 1], allJoints[i], o=[0, 0, 0], w=True,
                                                   aim=aimValue, u=objValue, wut="object", wuo=loc[0]))
                    cmds.delete(loc[0])
                    cmds.makeIdentity(allJoints[i], a=True, t=1, r=1, s=1, n=0, pn=1)
                    # parent joint.
                    cmds.parent(allJoints[i + 1], allJoints[i])
                    cmds.setAttr(allJoints[i + 1] + '.jointOrientX', 0)
                    cmds.setAttr(allJoints[i + 1] + '.jointOrientY', 0)
                    cmds.setAttr(allJoints[i + 1] + '.jointOrientZ', 0)
                    cmds.xform(allJoints[i + 1], ro=[0, 0, 0])
                else:
                    cmds.setAttr(allJoints[i] + '.jointOrientX', 0)
                    cmds.setAttr(allJoints[i] + '.jointOrientY', 0)
                    cmds.setAttr(allJoints[i] + '.jointOrientZ', 0)
                    cmds.xform(allJoints[i], ro=[0, 0, 0])
        else:
            raise RuntimeError('%s has no children...' % sel[x])


def aimConstraintParent(aimValue, objValue, sel=None):
    """
    do create aimConstraint according to ui based axis and delete constraint
    then parent first selected object and freeze transformation.
    :param sel: list (joint)
    :param aimValue: list ([1,0,0])
    :param objValue: list ([1,0,0])
    :return: aimConstraint (deleted.)
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if len(sel) != 2:
        cmds.warning('please select two objects...')
        return False
    cmds.select(cl=True)
    # create locator and snap on selection one.
    loc = cmds.spaceLocator(n='TempLocatorForObjectUpOrientation')
    cmds.delete(cmds.parentConstraint(sel[1], loc[0]))
    if objValue == [1, 0, 0]:
        cmds.move(3, 0, 0, loc[0], r=True, os=True, wd=True)
    if objValue == [0, 1, 0]:
        cmds.move(0, 3, 0, loc[0], r=True, os=True, wd=True)
    if objValue == [0, 0, 1]:
        cmds.move(0, 0, 3, loc[0], r=True, os=True, wd=True)
    cmds.delete(cmds.aimConstraint(sel[0], sel[1], o=[0, 0, 0], w=True, aim=aimValue, u=objValue,
                                   wut="object", wuo=loc[0]))
    # parent joint.
    cmds.parent(sel[0], sel[1])
    cmds.makeIdentity(sel[1], a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.setAttr(sel[0] + '.jointOrientX', 0)
    cmds.setAttr(sel[0] + '.jointOrientY', 0)
    cmds.setAttr(sel[0] + '.jointOrientZ', 0)
    # delete locator.
    cmds.delete(loc[0])
    cmds.select(sel[1])


def aimConstraint(aimValue, objValue, sel=None):
    """
    do create aim constraint according to ui based axis and delete constraint.
    and freeze transform second selected joint.
    :param sel: list (joint)
    :param aimValue: list ([1,0,0])
    :param objValue: list ([1,0,0])
    :return: aimConstraint (deleted.)
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if len(sel) != 2:
        cmds.warning('please select two objects...')
        return False
    cmds.select(cl=True)
    # create locator and snap on selection one.
    loc = cmds.spaceLocator(n='TempLocatorForObjectUpOrientation')
    cmds.delete(cmds.parentConstraint(sel[1], loc[0]))
    if objValue == [1, 0, 0]:
        cmds.move(3, 0, 0, loc[0], r=True, os=True, wd=True)
    if objValue == [0, 1, 0]:
        cmds.move(0, 3, 0, loc[0], r=True, os=True, wd=True)
    if objValue == [0, 0, 1]:
        cmds.move(0, 0, 3, loc[0], r=True, os=True, wd=True)
    cmds.delete(cmds.aimConstraint(sel[0], sel[1], o=[0, 0, 0], w=True, aim=aimValue, u=objValue,
                                   wut="object", wuo=loc[0]))
    cmds.makeIdentity(sel[1], a=True, t=1, r=1, s=1, n=0, pn=1)
    # delete locator.
    cmds.delete(loc[0])
    cmds.select(sel[1])


def noneOrient(sel=None):
    """
    set zero orientation of all selected joints.
    :param sel: list (joint)
    :return: zero orientation.
    """
    if not sel:
        sel = cmds.ls(sl=True, type='joint')
    if not sel:
        cmds.warning('no joints in selection...')
        return False
    for i in range(len(sel)):
        cmds.setAttr(sel[i] + '.jointOrientX', 0)
        cmds.setAttr(sel[i] + '.jointOrientY', 0)
        cmds.setAttr(sel[i] + '.jointOrientZ', 0)


def multiPointConstraint(cbVal, sel=None):
    """
    point constraint all selected item with last selected object.
    :param sel: list (joint)
    :param cbVal: bool (joint)
    :return: point constraint.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        cmds.warning('no objects selected...')
        return False
    if cbVal:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.pointConstraint(parentObj, sel[i], mo=True)
    else:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.pointConstraint(parentObj, sel[i])


def multiOrientConstraint(cbVal, sel=None):
    """
    orient constraint all selected item with last selected object.
    :param sel: list (joint)
    :param cbVal: bool (joint)
    :return: orient constraint.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        cmds.warning('no objects selected...')
        return False
    if cbVal:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.orientConstraint(parentObj, sel[i], mo=True)
    else:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.orientConstraint(parentObj, sel[i])


def multiParentConstraint(cbVal, sel=None):
    """
    parent constraint all selected item with last selected object.
    :param sel: list (joint)
    :param cbVal: bool (joint)
    :return: parent constraint
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        cmds.warning('no objects selected...')
        return False
    if cbVal:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.parentConstraint(parentObj, sel[i], mo=True)
    else:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.parentConstraint(parentObj, sel[i])
