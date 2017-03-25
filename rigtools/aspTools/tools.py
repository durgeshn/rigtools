from maya import cmds as cmds
from pymel import core as pm

from rigtools.utils import constraint
from rigtools.utils import mesure
from rigtools import maya_utils


def asIKCtlOriChange(joint, controller):
    """
    change ik controller orientation as local (getting joint orientation for reference)
    :param joint: string
    :param controller: string
    :return: controller
    """
    cmds.select(cl=True)
    tempLoc = cmds.spaceLocator()
    tempLoc1 = cmds.spaceLocator()
    cmds.select(cl=True)
    cmds.delete(cmds.parentConstraint(joint, tempLoc))
    cmds.delete(cmds.parentConstraint(joint, tempLoc1))
    cmds.parent(tempLoc, 'IKOffset' + controller[2:])
    listParents = cmds.listRelatives(controller, c=True)
    for i in range(1, len(listParents)):
        cmds.parent(listParents[i], tempLoc[0])
    cmds.delete(cmds.parentConstraint(tempLoc1, 'IKExtra' + controller[2:]))
    for i in range(1, len(listParents)):
        cmds.parent(listParents[i], controller)
    cmds.delete(tempLoc, tempLoc1)
    cmds.select(cl=True)

    # Add Hand Ik Extra Group Rotation value In Build Pose.
    GetAttrs = cmds.getAttr('buildPose.udAttr')
    qExtra = cmds.xform('IKExtra' + controller[2:], q=True, os=True, ro=True)
    newAttrss = GetAttrs.replace('xform -os -t 0 0 0 -ro 0 0 0 %s;' % ('IKExtra' + controller[2:]),
                                 'xform -os -t 0 0 0 -ro %f %f %f %s;' % (
                                     qExtra[0], qExtra[1], qExtra[2], 'IKExtra' + controller[2:]))
    cmds.setAttr('buildPose.udAttr', newAttrss, type="string")
    cmds.select(controller, r=True)
    print ('{0} orientation changed... '.format(controller)),
    return controller


def changeDrawStyleOfExtraJoints():
    """
    none draw style of unused joints in asp rig tool.
    :return: unusedJoints
    """
    with maya_utils.UndoChunkOpen('hide extra joints'):
        unusedJoints = cmds.ls('FKX*', 'IKX*', 'FKOffset*', type='joint')
        for each in unusedJoints:
            cmds.setAttr(each + '.drawStyle', 2)
        return unusedJoints


def fkCtlInIkSpine(startCtl, endCtl, hipCtlGrps, ctlName='Fk_Spine', ctlNum=4):
    """
    create fk controllers in advance skeleton ik spine setup.
    :param startCtl: string
    :param endCtl: string
    :param hipCtlGrps: list
    :param ctlName: string (keyable)
    :param ctlNum: int (number of controllers which you want)
    :return: fk controllers
    """
    loc = []
    for i in range(ctlNum + 1):
        newLoc = pm.spaceLocator(p=[0, 0, 0])
        loc.append(newLoc)

    # get length between start ctl and end ctl.
    pos = mesure.distanceCompareBetweenTwoObjects(startCtl, endCtl)
    length = mesure.getLength(pos[0], pos[1], pos[2])
    dividedLength = length / ctlNum

    for i in range(len(loc)):
        if i == 0:
            pm.delete(pm.parentConstraint(startCtl, loc[i]))
            constraint.aimConstraint([1, 0, 0], [0, 0, 1], [endCtl, str(loc[i])], freeze=False)
        else:
            setValX = dividedLength
            pm.parent(loc[i], loc[i - 1])
            loc[i].t.set(setValX, 0, 0)
            loc[i].r.set(0, 0, 0)
            setValX += dividedLength

    # create controllers.
    ctrls = []
    ctrlGrps = []
    ctrlGrpFollows = []
    for i in range(len(loc[:-1])):
        ctr = pm.modeling.circle(n=ctlName + str(i + 1), nrx=0, nry=1, nrz=0, ch=False)
        ctrls.append(ctr[0])
        ctrGrpExtra = pm.group(em=True, n=ctlName + str(i + 1) + '_Extra')
        ctrGrp = pm.group(em=True, n=ctlName + str(i + 1) + '_Grp')
        ctrlGrps.append(ctrGrp)
        ctrGrpFollow = pm.group(em=True, n=ctlName + str(i + 1) + '_Grp' + '_Follow')
        ctrlGrpFollows.append(ctrGrpFollow)
        pm.parent(ctr[0], ctrGrpExtra)
        pm.parent(ctrGrpExtra, ctrGrp)
        pm.parent(ctrGrp, ctrGrpFollow)
        pm.delete(pm.pointConstraint(loc[i], ctrGrpFollow))

    for i in range(2, len(ctrlGrpFollows)):
        pm.parentConstraint(ctrls[i - 1], ctrlGrpFollows[i], mo=True)

    # To put New controller in their corresponding Grp.
    pm.parentConstraint(ctrls[-1], 'IKOffset' + endCtl[2:], mo=True)
    pm.parentConstraint(ctrls[0], hipCtlGrps[0], mo=True)
    pm.parentConstraint(ctrls[0], hipCtlGrps[1], mo=True)
    pm.parentConstraint(startCtl, ctrlGrps[0])

    for each in range(len(ctrlGrpFollows)):
        pm.parent(ctrlGrpFollows[each], 'IKRootConstraint')
        pm.connectAttr('FKIKSpine_M.FKIKBlend', ctrlGrpFollows[each] + '.visibility')

    pm.parentConstraint('HipSwinger_M', 'IKOffset' + startCtl[2:], mo=True)
    pm.delete(loc)
