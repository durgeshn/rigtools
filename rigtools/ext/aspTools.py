import maya.cmds as cmds
import pymel.core as pm


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
    return controller


def changeDrawStyleOfExtraJoints():
    """
    none draw style of unused joints in asp rig tool.
    :return: unusedJoints
    """
    unusedJoints = cmds.ls('FKX*', 'IKX*', 'FKOffset*', type='joint')
    for each in unusedJoints:
        cmds.setAttr(each + '.drawStyle', 2)
    return unusedJoints


def addFingerAttributes():
    driver = ['Fingers_L']
    # fingers = ['Fingers_L', 'Fingers_R']
    attributes = ['_Scrunch', '_Twist', '_Lean', '_Scale']
    fingerBranch = ['Index', 'Middle', 'Ring', 'Pinky', 'Thumb']
    dispAttr = '_'
    for i in range(len(driver)):
        for x in range(len(attributes)):
            cmds.addAttr(driver[i], ln=dispAttr, at="enum", en=attributes[x][1:], k=True)
            cmds.setAttr(driver[i] + '.' + dispAttr, l=True)
            for z in range(len(fingerBranch)):
                cmds.addAttr(driver[i], ln=fingerBranch[z] + attributes[x], at="double", k=True)
            dispAttr += '_'


# scrunch attribute connections.
def addScrunch(attribute, controllers, axis='ry'):
    """
    add scrunch connections on controllers upper group.
    :param attribute: string
    :param controllers: list
    :param axis: string ('rx' or 'ry' or 'rz')
    :return: connections.
    """
    for a in range(len(controllers)):
        if a == 0:
            pma = pm.createNode('plusMinusAverage', ss=True, n='pma_' + controllers[a])
            pm.connectAttr(attribute, pma + '.input1D[0]', f=True)
            md = pm.createNode('multiplyDivide', ss=True, n='md_' + controllers[a])
            pm.connectAttr(pma + '.output1D', md + '.input1X', f=True)
            cmds.setAttr(md + '.input2X', -1)
            parentGrp = controllers[a].getParent()
            pm.connectAttr(md + '.outputX', parentGrp + '.' + axis, f=True)
        else:
            pma = pm.createNode('plusMinusAverage', ss=True, n='pma_' + controllers[a])
            pm.connectAttr(attribute, pma + '.input1D[0]', f=True)
            parentGrp = controllers[a].getParent()
            pm.connectAttr(pma + '.output1D', parentGrp + '.' + axis, f=True)
    print ('---- "%s" ----    connections done.....' % attribute),


# add finger attribute connections.
def addFingerAttributeConnections(attribute, controllers, axis='rx'):
    """
    add twist connections on controllers upper group.
    :param attribute: string
    :param controllers: list
    :param axis: string ('rx' or 'ry' or 'rz' or 'tx' or 'ty' or 'tz')
    :return: connections.
    """
    for a in range(len(controllers)):
        parentGrp = controllers[a].getParent()
        pm.connectAttr(attribute, parentGrp + "." + axis)
    print ('---- "%s" ----    connections done.....' % attribute),
