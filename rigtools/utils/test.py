import maya.cmds as cmds
import pymel.core as pm


def fkCtlInIkSpine(startCtl, endCtl, hipCtlGrps, ctlName='Fk_Spine', ctlNum=5):
    """
    create fk controllers in advance skeleton ik spine setup.
    :param startCtl: string
    :param endCtl: string
    :param hipCtlGrps: list
    :param ctlName: string (keyable)
    :return: fk controllers
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

    loc = [loc1, loc2, loc3, loc4, loc5]
    ctrls = []
    ctrlGrps = []
    for i in range(len(loc[:-1])):
        ctr = pm.modeling.circle(n=ctlName + str(i + 1), nrx=0, nry=1, nrz=0, ch=False)
        ctrls.append(ctr[0])
        ctrGrpExtra = pm.group(em=True, n=ctlName + str(i + 1) + '_Extra')
        ctrGrp = pm.group(em=True, n=ctlName + str(i + 1) + '_Grp')
        ctrGrpFollow = pm.group(em=True, n=ctlName + str(i + 1) + '_Grp' + '_Follow')
        pm.parent(ctr[0], ctrGrpExtra)
        pm.parent(ctrGrpExtra, ctrGrp)
        pm.parent(ctrGrp, ctrGrpFollow)
        ctrlGrps.append(ctrGrpFollow)
        pm.delete(pm.pointConstraint(loc[i], ctrGrpFollow))

    for i in range(2, len(ctrlGrps)):
        pm.parentConstraint(ctrls[i - 1], ctrlGrps[i], mo=True)

    # To put New controller in their corresponding Grp.

    Ikspinectrs = pm.ls('*IKOffsetSpine*')
    spine_ctr = Ikspinectrs[-1]
    pm.parentConstraint('Fk_Spine4', spine_ctr, mo=True)
    pm.parentConstraint('Fk_Spine1', hipCtlGrps[0], mo=True)
    pm.parentConstraint('Fk_Spine1', hipCtlGrps[1], mo=True)
    pm.parentConstraint('IKSpine1_M', 'Fk_Spine1_Grp')

    for each in range(len(ctrlGrps)):
        pm.parent(ctrlGrps[each], 'IKRootConstraint')
        pm.connectAttr('FKIKSpine_M.FKIKBlend', ctrlGrps[each] + '.visibility')

    pm.parentConstraint('HipSwinger_M', 'IKOffsetSpine1_M', mo=True)

    # To Delete Dummy Locator

    pm.delete(loc)
