import maya.cmds as cmds
from rigtools.ext import aspTools
# from mainWindow import aspIkOriChangeUIFile

reload(aspTools)


def aspIkOriChangeWindowConn():
    """
    aspIkOriChangeConn UI connections.
    :return: ui connection
    """
    if cmds.window('aspIKOriChangeWindow', exists=True):
        cmds.deleteUI('aspIKOriChangeWindow')
    aspIkOriChangeUI = cmds.loadUI(f=aspIkOriChangeUIFile)
    cmds.showWindow(aspIkOriChangeUI)
    cmds.button('aspIkOriJntLd_btn', e=True,
                c='from rigtools.ui import ui_fill;ui_fill.addInTextField("aspIkOriJnt_LE")')
    cmds.button('aspIkOriCtlLd_btn', e=True,
                c='from rigtools.ui import ui_fill;ui_fill.addInTextField("aspIkOriCtl_LE")')
    cmds.button('aspIkOriSet_btn', e=True, c='aspToolsUiConn.aspIkOriChangeConn()')


def aspIkOriChangeConn():
    joint = cmds.textField('aspIkOriJnt_LE', q=True, tx=True)
    controller = cmds.textField('aspIkOriCtl_LE', q=True, tx=True)
    aspTools.asIKCtlOriChange(joint, controller)


def changeDrawStyleOfExtraJointsConn():
    """
    changeDrawStyleOfExtraJoints UI connections.
    :return: ui connection
    """
    aspTools.changeDrawStyleOfExtraJoints()


def addIKArmFollowSwitch():
    """
    add follow switch in ik arm controller.
    :return: follow attribute.
    """
    cmds.deleteAttr("IKArm_L", "IKArm_R", at="follow")
    cmds.delete("IKOffsetArm_L_parentConstraint1", "IKOffsetArm_R_parentConstraint1")
    cmds.addAttr("IKArm_L", "IKArm_R", ln="Follow", at='enum', en="Global:Chest:Shoulder:Hip:Head", k=True)
    cmds.parentConstraint("IKOffsetArm_LStatic", "IKOffsetArm_L", mo=True)
    cmds.parentConstraint("Chest_M", "IKOffsetArm_L", mo=True)
    cmds.parentConstraint("Scapula_L", "IKOffsetArm_L", mo=True)
    cmds.parentConstraint("Root_M", "IKOffsetArm_L", mo=True)
    cmds.parentConstraint("Head_M", "IKOffsetArm_L", mo=True)
    cmds.parentConstraint("IKOffsetArm_RStatic", "IKOffsetArm_R", mo=True)
    cmds.parentConstraint("Chest_M", "IKOffsetArm_R", mo=True)
    cmds.parentConstraint("Scapula_R", "IKOffsetArm_R", mo=True)
    cmds.parentConstraint("Root_M", "IKOffsetArm_R", mo=True)
    cmds.parentConstraint("Head_M", "IKOffsetArm_R", mo=True)


def addPoleArmFollowSwitch():
    """
    add follow switch in pole arm.
    :return: follow switch.
    """
    cmds.deleteAttr("PoleArm_L", "PoleArm_R", at="follow")
    cmds.delete("PoleOffsetArm_L_parentConstraint1", "PoleOffsetArm_R_parentConstraint1")
    cmds.addAttr("PoleArm_L", "PoleArm_R", ln="Follow", at='enum', en="Global:Chest:Arm", k=True)
    cmds.parentConstraint("PoleOffsetArm_LStatic", "PoleOffsetArm_L", mo=True)
    cmds.parentConstraint("Chest_M", "PoleOffsetArm_L", mo=True)
    cmds.parentConstraint("IKArm_L", "PoleOffsetArm_L", mo=True)
    cmds.parentConstraint("PoleOffsetArm_RStatic", "PoleOffsetArm_R", mo=True)
    cmds.parentConstraint("Chest_M", "PoleOffsetArm_R", mo=True)
    cmds.parentConstraint("IKArm_R", "PoleOffsetArm_R", mo=True)
