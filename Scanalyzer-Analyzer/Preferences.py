# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName(_fromUtf8("Preferences"))
        Preferences.setWindowModality(QtCore.Qt.ApplicationModal)
        Preferences.resize(382, 302)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/preferences-system.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Preferences.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Preferences)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Controls_Toggle = QtGui.QCheckBox(Preferences)
        self.Controls_Toggle.setObjectName(_fromUtf8("Controls_Toggle"))
        self.gridLayout_2.addWidget(self.Controls_Toggle, 1, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(Preferences)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Plate_List = QtGui.QListWidget(self.groupBox)
        self.Plate_List.setObjectName(_fromUtf8("Plate_List"))
        self.gridLayout.addWidget(self.Plate_List, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(Preferences)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Preferences.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(_translate("Preferences", "Preferences", None))
        self.Controls_Toggle.setText(_translate("Preferences", "Toggle Positive/Negative Control Selection", None))
        self.groupBox.setTitle(_translate("Preferences", "Plate Layouts", None))

import Scanalyzer_analyzer_rc
