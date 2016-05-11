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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(993, 628)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.File_Selector_Box = QtGui.QComboBox(self.centralwidget)
        self.File_Selector_Box.setObjectName(_fromUtf8("File_Selector_Box"))
        self.gridLayout_2.addWidget(self.File_Selector_Box, 0, 0, 1, 2)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.Id_List = QtGui.QListWidget(self.groupBox)
        self.Id_List.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Id_List.sizePolicy().hasHeightForWidth())
        self.Id_List.setSizePolicy(sizePolicy)
        self.Id_List.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.Id_List.setObjectName(_fromUtf8("Id_List"))
        self.gridLayout_4.addWidget(self.Id_List, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Analyze_Btn = QtGui.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Analyze_Btn.sizePolicy().hasHeightForWidth())
        self.Analyze_Btn.setSizePolicy(sizePolicy)
        self.Analyze_Btn.setObjectName(_fromUtf8("Analyze_Btn"))
        self.horizontalLayout_2.addWidget(self.Analyze_Btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.New_Class_Btn = QtGui.QPushButton(self.centralwidget)
        self.New_Class_Btn.setObjectName(_fromUtf8("New_Class_Btn"))
        self.horizontalLayout.addWidget(self.New_Class_Btn)
        self.Save_Class_Btn = QtGui.QPushButton(self.centralwidget)
        self.Save_Class_Btn.setObjectName(_fromUtf8("Save_Class_Btn"))
        self.horizontalLayout.addWidget(self.Save_Class_Btn)
        self.Delete_Class_Btn = QtGui.QPushButton(self.centralwidget)
        self.Delete_Class_Btn.setObjectName(_fromUtf8("Delete_Class_Btn"))
        self.horizontalLayout.addWidget(self.Delete_Class_Btn)
        self.Reset_Plate_Btn = QtGui.QPushButton(self.centralwidget)
        self.Reset_Plate_Btn.setObjectName(_fromUtf8("Reset_Plate_Btn"))
        self.horizontalLayout.addWidget(self.Reset_Plate_Btn)
        self.gridLayout_6.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.Load_Layout_Btn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Load_Layout_Btn.sizePolicy().hasHeightForWidth())
        self.Load_Layout_Btn.setSizePolicy(sizePolicy)
        self.Load_Layout_Btn.setMinimumSize(QtCore.QSize(80, 0))
        self.Load_Layout_Btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Load_Layout_Btn.setObjectName(_fromUtf8("Load_Layout_Btn"))
        self.horizontalLayout_3.addWidget(self.Load_Layout_Btn)
        self.Save_Layout_Btn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Save_Layout_Btn.sizePolicy().hasHeightForWidth())
        self.Save_Layout_Btn.setSizePolicy(sizePolicy)
        self.Save_Layout_Btn.setMinimumSize(QtCore.QSize(80, 0))
        self.Save_Layout_Btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Save_Layout_Btn.setObjectName(_fromUtf8("Save_Layout_Btn"))
        self.horizontalLayout_3.addWidget(self.Save_Layout_Btn)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.Treatments_List = QtGui.QListWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Treatments_List.sizePolicy().hasHeightForWidth())
        self.Treatments_List.setSizePolicy(sizePolicy)
        self.Treatments_List.setObjectName(_fromUtf8("Treatments_List"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.Treatments_List)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.Set_Positive_Control = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Set_Positive_Control.sizePolicy().hasHeightForWidth())
        self.Set_Positive_Control.setSizePolicy(sizePolicy)
        self.Set_Positive_Control.setMinimumSize(QtCore.QSize(130, 0))
        self.Set_Positive_Control.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Set_Positive_Control.setObjectName(_fromUtf8("Set_Positive_Control"))
        self.horizontalLayout_4.addWidget(self.Set_Positive_Control)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.Set_Negative_Control = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Set_Negative_Control.sizePolicy().hasHeightForWidth())
        self.Set_Negative_Control.setSizePolicy(sizePolicy)
        self.Set_Negative_Control.setMinimumSize(QtCore.QSize(130, 0))
        self.Set_Negative_Control.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Set_Negative_Control.setObjectName(_fromUtf8("Set_Negative_Control"))
        self.horizontalLayout_4.addWidget(self.Set_Negative_Control)
        self.formLayout.setLayout(1, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_4)
        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(550, 380))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(self.groupBox_3)
        self.webView.setMinimumSize(QtCore.QSize(0, 216))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuWell_Analysis_Selector = QtGui.QMenu(self.menubar)
        self.menuWell_Analysis_Selector.setObjectName(_fromUtf8("menuWell_Analysis_Selector"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen_Files = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Files.setIcon(icon)
        self.actionOpen_Files.setObjectName(_fromUtf8("actionOpen_Files"))
        self.actionCreate_Analysis_Class = QtGui.QAction(MainWindow)
        self.actionCreate_Analysis_Class.setObjectName(_fromUtf8("actionCreate_Analysis_Class"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.action_Undo = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../../AppData/Local/Continuum/Anaconda3/Lib/site-packages/PyQt4/examples/mainwindows/dockwidgets/images/undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Undo.setIcon(icon2)
        self.action_Undo.setObjectName(_fromUtf8("action_Undo"))
        self.actionReset_Plate = QtGui.QAction(MainWindow)
        self.actionReset_Plate.setObjectName(_fromUtf8("actionReset_Plate"))
        self.actionSave_Class = QtGui.QAction(MainWindow)
        self.actionSave_Class.setObjectName(_fromUtf8("actionSave_Class"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/preferences-system.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon3)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.menuWell_Analysis_Selector.addAction(self.actionOpen_Files)
        self.menuWell_Analysis_Selector.addSeparator()
        self.menuWell_Analysis_Selector.addAction(self.actionPreferences)
        self.menuWell_Analysis_Selector.addAction(self.actionExit)
        self.menubar.addAction(self.menuWell_Analysis_Selector.menuAction())
        self.toolBar.addAction(self.actionOpen_Files)
        self.toolBar.addAction(self.actionPreferences)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Scanalyzer Analyzer", None))
        self.groupBox.setTitle(_translate("MainWindow", "Snapshot ID Tags", None))
        self.Analyze_Btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>This will analyze all of the files in the file list according to the defined treatments for each Snapshot ID Tag. Wells without a treatment defined will be lumped together for each Snapshot ID Tag.</p></body></html>", None))
        self.Analyze_Btn.setStatusTip(_translate("MainWindow", "Analyze files using current treatments", None))
        self.Analyze_Btn.setText(_translate("MainWindow", "Analyze Files", None))
        self.New_Class_Btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Creates a new treatment for all of the selected Snapshot ID Tag\'s. You will be prompted to enter a name for the treatment after clicking. </p></body></html>", None))
        self.New_Class_Btn.setStatusTip(_translate("MainWindow", "Create a new treatment for selected ID\'s.", None))
        self.New_Class_Btn.setText(_translate("MainWindow", "Create New Class", None))
        self.Save_Class_Btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Saves the current treatment with all selected wells. If a well is selected that was previously saved to another treatment it will be removed from that treatment and applied to the most recently saved treatment.</p></body></html>", None))
        self.Save_Class_Btn.setStatusTip(_translate("MainWindow", "Save current treatment.", None))
        self.Save_Class_Btn.setText(_translate("MainWindow", "Save Class", None))
        self.Delete_Class_Btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Deletes the currently selected treatment from the currently selected Snapshot ID Tag\'s. This will remove the treatment and all associated wells. </p></body></html>", None))
        self.Delete_Class_Btn.setStatusTip(_translate("MainWindow", "Delete treatment from current ID\'s", None))
        self.Delete_Class_Btn.setText(_translate("MainWindow", "Delete Class", None))
        self.Reset_Plate_Btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Resets the treatments for the current Snapshot ID Tag. This will remove all of the saved treatment classes as well as their associated wells. </p></body></html>", None))
        self.Reset_Plate_Btn.setStatusTip(_translate("MainWindow", "Reset current plate treatments.", None))
        self.Reset_Plate_Btn.setText(_translate("MainWindow", "Reset Plate", None))
        self.Load_Layout_Btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Opens the layout loader dialog menu. In this menu you will be able to select layouts existing within the default layouts file. This layout will be applied to all currently selected Snapshot ID Tag\'s. You may also choose to select a different layout file if you have layouts stored in another location. </p></body></html>", None))
        self.Load_Layout_Btn.setStatusTip(_translate("MainWindow", "Load predefined treatment layout for selected ID\'s.", None))
        self.Load_Layout_Btn.setText(_translate("MainWindow", "Load layout", None))
        self.Save_Layout_Btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Saves the current treatment names and associated wells to a new layout. You will be prompted to name the layout after clicking. </p></body></html>", None))
        self.Save_Layout_Btn.setStatusTip(_translate("MainWindow", "Save current treatments as new layout.", None))
        self.Save_Layout_Btn.setText(_translate("MainWindow", "Save Layout", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Treatments", None))
        self.Set_Positive_Control.setToolTip(_translate("MainWindow", "<html><head/><body><p>Sets the currently selected treatment as the positive control. This value is only used for calculation of Z Factor (if selected) in analysis. </p></body></html>", None))
        self.Set_Positive_Control.setStatusTip(_translate("MainWindow", "Set treatment as positive control.", None))
        self.Set_Positive_Control.setText(_translate("MainWindow", "Set as Positive Control", None))
        self.Set_Negative_Control.setToolTip(_translate("MainWindow", "<html><head/><body><p>Sets the currently selected treatment as the negative control. This value is only used for calculation of Z Factor (if selected) in analysis. </p></body></html>", None))
        self.Set_Negative_Control.setStatusTip(_translate("MainWindow", "Set treatment as negative control.", None))
        self.Set_Negative_Control.setText(_translate("MainWindow", "Set as Negative Control", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Plate Layout", None))
        self.menuWell_Analysis_Selector.setTitle(_translate("MainWindow", "&File", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionOpen_Files.setText(_translate("MainWindow", "&Open", None))
        self.actionOpen_Files.setToolTip(_translate("MainWindow", "Open", None))
        self.actionOpen_Files.setStatusTip(_translate("MainWindow", "Choose files to open for analysis.", None))
        self.actionOpen_Files.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionCreate_Analysis_Class.setText(_translate("MainWindow", "Create Analysis Class", None))
        self.actionCreate_Analysis_Class.setToolTip(_translate("MainWindow", "Create a new class for grouping wells in analysis", None))
        self.actionExit.setText(_translate("MainWindow", "&Exit", None))
        self.actionExit.setStatusTip(_translate("MainWindow", "Close the Scanalyzer Analyzer", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.action_Undo.setText(_translate("MainWindow", "&Undo", None))
        self.actionReset_Plate.setText(_translate("MainWindow", "Reset Plate", None))
        self.actionSave_Class.setText(_translate("MainWindow", "Save Class", None))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences", None))

from PyQt4 import QtWebKit
import Scanalyzer_analyzer_rc
