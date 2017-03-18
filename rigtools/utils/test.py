import maya.cmds as cmds
import pymel.core as pm


def fkCtlInIkSpine(startCtl, endCtl, hipCtlGrps, ctlName='Fk_Spine'):
    """
    Create FK controller in Advance skeleton IK Spine.
    :return: fkControllers.
    """
    # create dummy locators.
    loc1 = pm.spaceLocator(p=[0, 0, 0])
    loc2 = pm.spaceLocator(p=[0, 0, 0])
    loc3 = pm.spaceLocator(p=[0, 0, 0])
    loc4 = pm.spaceLocator(p=[0, 0, 0])
    loc5 = pm.spaceLocator(p=[0, 0, 0])
    pm.pointConstraint(loc1, loc5, loc3)
    pm.pointConstraint(loc1, loc3, loc2)
    pm.pointConstraint(loc3, loc5, loc4)
    pm.parentConstraint(endCtl, loc5)
    pm.parentConstraint(startCtl, loc1)

    loc = ['dummy1', 'dummy2', 'dummy3', 'dummy4', 'dummy5']
    ctrls = []
    ctrlGrps = []
    for i in range(4):
        ctr = pm.circle(n=ctlName + str(i + 1), nrx=0, nry=1, nrz=0, ch=False)
        ctrls.append(ctr[0])
        ctrGrpExtra = cmds.group(ctr, n=ctlName + str(i + 1) + '_Extra')
        ctrGrp = cmds.group(ctrGrpExtra, n=ctlName + str(i + 1) + '_Grp')
        ctrGrpFollow = cmds.group(ctrGrp, n=ctlName + str(i + 1) + '_Grp' + '_Follow')
        ctrlGrps.append(ctrGrpFollow)
        cmds.delete(cmds.pointConstraint(loc[i], ctrGrpFollow))

    k = ctrls[1:3]
    l = ctrlGrps[2:]
    l.reverse()
    k.reverse()
    for (x, y) in zip(l, k):
        cmds.parentConstraint(y, x, mo=True)

    # To put New controller in their corresponding Grp

    Ikspinectrs = cmds.ls('*IKOffsetSpine*')
    spine_ctr = Ikspinectrs[-1]
    cmds.parentConstraint('Fk_Spine4', spine_ctr, mo=True)
    cmds.parentConstraint('Fk_Spine1', 'FKOffsetScapula1_L', mo=True)
    cmds.parentConstraint('Fk_Spine1', 'FKOffsetScapula1_R', mo=True)
    cmds.parentConstraint('IKSpine1_M', 'Fk_Spine1_Grp')

    for each in range(len(ctrlGrps)):
        cmds.parent(ctrlGrps[each], 'IKRootConstraint')
        cmds.connectAttr('FKIKSpine_M.FKIKBlend', ctrlGrps[each] + '.visibility')

    cmds.parentConstraint('HipSwinger_M', 'IKOffsetSpine1_M', mo=True)

    # To Delete Dummy Loctor

    cmds.delete(loc)
