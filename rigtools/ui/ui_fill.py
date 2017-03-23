import pymel.core as pm


def fillLineEdit(lineEdit, sel=None):
    """
    add selection in window line edit.
    :param lineEdit: string
    :param sel: list
    :return: line edit fill
    """
    if not sel:
        sel = pm.ls(sl=True)
    if not sel:
        raise RuntimeError('Please select only one object')
    elif len(sel) > 1:
        raise RuntimeError('more than one objects selected.')
    lineEdit.setText(str(sel[0]))
