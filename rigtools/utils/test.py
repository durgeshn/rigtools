# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T:\amol\From_Prafull\aspFingerAttributes.ui'
#
# Created: Wed Mar 15 15:17:13 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys
from PySide.QtGui import QApplication, QMainWindow


class Ui_FingerAttributeWindow(QMainWindow):
    def __init__(self):
        super(Ui_FingerAttributeWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("FingerAttributeWindow")
        self.resize(367, 243)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.aspFaTwist_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaTwist_cb.setObjectName("aspFaTwist_cb")
        self.gridLayout_3.addWidget(self.aspFaTwist_cb, 0, 1, 1, 1)
        self.aspFaLean_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaLean_cb.setObjectName("aspFaLean_cb")
        self.gridLayout_3.addWidget(self.aspFaLean_cb, 1, 0, 1, 1)
        self.aspFaScale_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaScale_cb.setObjectName("aspFaScale_cb")
        self.gridLayout_3.addWidget(self.aspFaScale_cb, 1, 1, 1, 1)
        self.aspFaRelax_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaRelax_cb.setObjectName("aspFaRelax_cb")
        self.gridLayout_3.addWidget(self.aspFaRelax_cb, 2, 0, 1, 1)
        self.aspFaScrunch_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaScrunch_cb.setObjectName("aspFaScrunch_cb")
        self.gridLayout_3.addWidget(self.aspFaScrunch_cb, 0, 0, 1, 1)
        self.aspFaFist_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaFist_cb.setObjectName("aspFaFist_cb")
        self.gridLayout_3.addWidget(self.aspFaFist_cb, 3, 0, 1, 1)
        self.aspFaReverse_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaReverse_cb.setObjectName("aspFaReverse_cb")
        self.gridLayout_3.addWidget(self.aspFaReverse_cb, 2, 1, 1, 1)
        self.aspFaCup_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaCup_cb.setObjectName("aspFaCup_cb")
        self.gridLayout_3.addWidget(self.aspFaCup_cb, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 2, 1)
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_2.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.aspFaLoadFingers_btn = QtGui.QPushButton(self.centralwidget)
        self.aspFaLoadFingers_btn.setObjectName("aspFaLoadFingers_btn")
        self.gridLayout.addWidget(self.aspFaLoadFingers_btn, 0, 2, 1, 1)
        self.aspFaFingerControllers_LE = QtGui.QLineEdit(self.centralwidget)
        self.aspFaFingerControllers_LE.setObjectName("aspFaFingerControllers_LE")
        self.gridLayout.addWidget(self.aspFaFingerControllers_LE, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.aspFaCreate_btn = QtGui.QPushButton(self.centralwidget)
        self.aspFaCreate_btn.setObjectName("aspFaCreate_btn")
        self.gridLayout_2.addWidget(self.aspFaCreate_btn, 4, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, FingerAttributeWindow):
        FingerAttributeWindow.setWindowTitle(
            QtGui.QApplication.translate("FingerAttributeWindow", "ASP Add Finger Attributes", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.aspFaTwist_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Twist", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaLean_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Lean", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaScale_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaRelax_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Relax", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaScrunch_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Scrunch", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaFist_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Fist", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaReverse_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Reverse", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaCup_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Cup", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("FingerAttributeWindow",
                                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                "p, li { white-space: pre-wrap; }\n"
                                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1) Select Finger Controllers in order like</p>\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">IndexFinger1, IndexFinger2, IndexFinger3</span></p>\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2) on check box for add selected attributes.</p>\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3) create.</p></body></html>",
                                                                None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaLoadFingers_btn.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Fingers:-", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaCreate_btn.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Create", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Ui_FingerAttributeWindow()
    test.show()
    sys.exit(app.exec_())
