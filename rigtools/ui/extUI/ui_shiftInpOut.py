# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T:\amol\bit_bucket\rigtools\rigtools\ui\extUI\ui_shiftInpOut.ui'
#
# Created: Thu Mar 23 12:43:01 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_ShiftInpOutConnWindow(object):
    def setupUi(self, ShiftInpOutConnWindow):
        ShiftInpOutConnWindow.setObjectName("ShiftInpOutConnWindow")
        ShiftInpOutConnWindow.resize(491, 300)
        self.centralwidget = QtGui.QWidget(ShiftInpOutConnWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.newShapeCreate_btn = QtGui.QPushButton(self.centralwidget)
        self.newShapeCreate_btn.setObjectName("newShapeCreate_btn")
        self.gridLayout_4.addWidget(self.newShapeCreate_btn, 1, 2, 1, 1)
        self.newShpName_LE = QtGui.QLineEdit(self.centralwidget)
        self.newShpName_LE.setObjectName("newShpName_LE")
        self.gridLayout_4.addWidget(self.newShpName_LE, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.shiftConnections_btn = QtGui.QPushButton(self.centralwidget)
        self.shiftConnections_btn.setObjectName("shiftConnections_btn")
        self.gridLayout_2.addWidget(self.shiftConnections_btn, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 4, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.srcOutLd_btn = QtGui.QPushButton(self.centralwidget)
        self.srcOutLd_btn.setObjectName("srcOutLd_btn")
        self.gridLayout.addWidget(self.srcOutLd_btn, 4, 3, 1, 1)
        self.destInpLd_btn = QtGui.QPushButton(self.centralwidget)
        self.destInpLd_btn.setObjectName("destInpLd_btn")
        self.gridLayout.addWidget(self.destInpLd_btn, 7, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 5, 2, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.destOut_LE = QtGui.QLineEdit(self.centralwidget)
        self.destOut_LE.setObjectName("destOut_LE")
        self.gridLayout.addWidget(self.destOut_LE, 8, 2, 1, 1)
        self.destInp_LE = QtGui.QLineEdit(self.centralwidget)
        self.destInp_LE.setObjectName("destInp_LE")
        self.gridLayout.addWidget(self.destInp_LE, 7, 2, 1, 1)
        self.destOutLd_btn = QtGui.QPushButton(self.centralwidget)
        self.destOutLd_btn.setObjectName("destOutLd_btn")
        self.gridLayout.addWidget(self.destOutLd_btn, 8, 3, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.srcInp_LE = QtGui.QLineEdit(self.centralwidget)
        self.srcInp_LE.setObjectName("srcInp_LE")
        self.gridLayout.addWidget(self.srcInp_LE, 1, 2, 1, 1)
        self.srcOut_LE = QtGui.QLineEdit(self.centralwidget)
        self.srcOut_LE.setObjectName("srcOut_LE")
        self.gridLayout.addWidget(self.srcOut_LE, 4, 2, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 5, 3, 1, 1)
        self.srcInpLd_btn = QtGui.QPushButton(self.centralwidget)
        self.srcInpLd_btn.setObjectName("srcInpLd_btn")
        self.gridLayout.addWidget(self.srcInpLd_btn, 1, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 1, 0, 1, 1)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 3, 0, 1, 1)
        ShiftInpOutConnWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ShiftInpOutConnWindow)
        QtCore.QMetaObject.connectSlotsByName(ShiftInpOutConnWindow)

    def retranslateUi(self, ShiftInpOutConnWindow):
        ShiftInpOutConnWindow.setWindowTitle(
            QtGui.QApplication.translate("ShiftInpOutConnWindow", "Shift Mesh Input Output Connections", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.newShapeCreate_btn.setText(
            QtGui.QApplication.translate("ShiftInpOutConnWindow", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(
            QtGui.QApplication.translate("ShiftInpOutConnWindow", "Create New Shapes on Selected Transform.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ShiftInpOutConnWindow", "Enter New Shape Name:-", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.shiftConnections_btn.setText(
            QtGui.QApplication.translate("ShiftInpOutConnWindow", "Shift Connections", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.srcOutLd_btn.setText(
            QtGui.QApplication.translate("ShiftInpOutConnWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.destInpLd_btn.setText(
            QtGui.QApplication.translate("ShiftInpOutConnWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ShiftInpOutConnWindow", "Destination Output Shape:-", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ShiftInpOutConnWindow", "Destination Input Shape:-", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.destOutLd_btn.setText(
            QtGui.QApplication.translate("ShiftInpOutConnWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ShiftInpOutConnWindow", "Source Output Shape:-", None,
                                                        QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ShiftInpOutConnWindow", "Get Source Shapes", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.srcInpLd_btn.setText(
            QtGui.QApplication.translate("ShiftInpOutConnWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ShiftInpOutConnWindow", "Source Input Shape:-", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ShiftInpOutConnWindow", "Get Destination Shapes", None,
                                                          QtGui.QApplication.UnicodeUTF8))
