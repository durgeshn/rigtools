import pymel.core as pm
import maya.cmds as cmds
from rigtools.utils import selection


def addInTextField(tField, sel=None):
    """
    add Text in Window Text Field.
    :param tField: str (textField Name)
    :param sel: str (text you want to add in text field)
    :return: textField fill
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        pm.warning('Please select one object.')
        return False
    sel = selection.getSelection()[0]
    pm.textField(tField, e=True, tx=sel)
