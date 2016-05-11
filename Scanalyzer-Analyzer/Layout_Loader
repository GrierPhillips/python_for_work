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

class Ui_Layout_Loader(object):
    def setupUi(self, Layout_Loader):
        Layout_Loader.setObjectName(_fromUtf8("Layout_Loader"))
        Layout_Loader.setWindowModality(QtCore.Qt.ApplicationModal)
        Layout_Loader.resize(400, 316)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Layout_Loader.setWindowIcon(icon)
        self.formLayout_2 = QtGui.QFormLayout(Layout_Loader)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(Layout_Loader)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.Change_Layout_Btn = QtGui.QToolButton(Layout_Loader)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Change_Layout_Btn.sizePolicy().hasHeightForWidth())
        self.Change_Layout_Btn.setSizePolicy(sizePolicy)
        self.Change_Layout_Btn.setMinimumSize(QtCore.QSize(130, 0))
        self.Change_Layout_Btn.setObjectName(_fromUtf8("Change_Layout_Btn"))
        self.horizontalLayout.addWidget(self.Change_Layout_Btn)
        self.formLayout_2.setLayout(1, QtGui.QFormLayout.LabelRole, self.horizontalLayout)
        self.groupBox = QtGui.QGroupBox(Layout_Loader)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Layouts_List = QtGui.QListWidget(self.groupBox)
        self.Layouts_List.setObjectName(_fromUtf8("Layouts_List"))
        self.gridLayout.addWidget(self.Layouts_List, 0, 0, 1, 1)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox)

        self.retranslateUi(Layout_Loader)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Layout_Loader.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Layout_Loader.reject)
        QtCore.QMetaObject.connectSlotsByName(Layout_Loader)

    def retranslateUi(self, Layout_Loader):
        Layout_Loader.setWindowTitle(_translate("Layout_Loader", "Load Layout", None))
        self.Change_Layout_Btn.setText(_translate("Layout_Loader", "Change Layouts File", None))
        self.groupBox.setTitle(_translate("Layout_Loader", "Saved Layouts", None))

import Scanalyzer_analyzer_rc
