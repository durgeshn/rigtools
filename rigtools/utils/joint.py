from maya import cmds as cmds


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
