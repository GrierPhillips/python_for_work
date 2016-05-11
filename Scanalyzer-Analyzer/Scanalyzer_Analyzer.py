#!/usr/bin/env python
"""
Scanalyzer Data Analyzer

Allows user to select multiple output files from the Scanalyzer, select 
individual plates within files, and assign layouts of treatments to these 
plates. These settings are then used for processing the output files and 
creating a clean summary file of the raw data and simple statistics for 
each treatment within a plate. 

Output is as an Excel file in the same directory as the original file sharing
the same name except with a .xlsx extension
"""

__author__ = "Grier Phillips"
__email__ = "GrierPhillips@gmail.com"
__status__ = "Prototype"
__version__ = "0.1.0"

import sys
from string import ascii_uppercase
from PyQt4 import QtCore, QtGui
from Maini_Window import Ui_MainWindow
from Layout_Loader import Ui_Layout_Loader
from Preferences import Ui_Preferences
import pandas as pd
import numpy as np
import os
import re
import json
from bs4 import BeautifulSoup

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		pd.set_option('io.hdf.default_format', 'table')
		self.Set_Negative_Control.hide()
		self.Set_Positive_Control.hide()
		self.webView.load(
			QtCore.QUrl.fromLocalFile(sys._MEIPASS + \
			'/24 Well.html'))
		self.File_Selector_Box.activated.connect(self.Select_File)
		self.actionOpen_Files.triggered.connect(self.Choose_File)
		self.actionPreferences.triggered.connect(self.Load_Preferences)
		self.Id_List.itemSelectionChanged.connect(self.Select_Id)
		self.Treatments_List.itemSelectionChanged.connect(self.Select_Treatment)
		self.New_Class_Btn.clicked.connect(self.New_Treatment)
		self.Reset_Plate_Btn.clicked.connect(self.Reset_Plate)
		self.Save_Class_Btn.clicked.connect(self.Save_Treatment)
		self.Delete_Class_Btn.clicked.connect(self.Delete_Treatment)
		self.Load_Layout_Btn.clicked.connect(self.Load_Layouts)
		self.Save_Layout_Btn.clicked.connect(self.Save_Layout)
		self.Analyze_Btn.clicked.connect(self.Analyze)
		self.Treatments_List.itemDoubleClicked.connect(self.Edit_Treatment)
		self.Treatments_List.itemChanged.connect(self.Save_Treatment)
		self.Set_Negative_Control.clicked.connect(self.Get_Negative_Control)
		self.Set_Positive_Control.clicked.connect(self.Get_Positive_Control)
                 	


	def Choose_File(self):
		if self.File_Selector_Box.count() == 0:
			self.slpath = QtGui.QFileDialog.getOpenFileNames(
				self, 'Choose Scanalyzer File', '', "csv (*.csv)", 
				QtGui.QFileDialog.DontUseNativeDialog)
			if self.slpath: 
				self.statusBar().showMessage("Scanalyzer CSV valid.")
				self.File_Selector_Box.addItems(self.slpath)
				self.Import_Data()
				self.Select_File()
		else:	
			self.additional_files = QtGui.QFileDialog.getOpenFileNames(
				self, 'Choose Scanalyzer File', '', "csv (*.csv)", 
				QtGui.QFileDialog.DontUseNativeDialog)
			duplicates = []
			for file in self.additional_files:
				if file in self.slpath:
					self.additional_files.remove(file)
					duplicates.append(file)
			if len(duplicates) > 0:
				self.Error = QtGui.QErrorMessage(self)
				self.Error.setWindowTitle('Error: Duplicate File!')
				self.Error.showMessage(
					'A file with that name has already been loaded.')
			self.slpath.extend(self.additional_files)
			if self.slpath: 
				self.statusBar().showMessage("Scanalyzer CSV's are Valid")
				self.File_Selector_Box.clear()
				self.Update_Labels()
				self.Import_Data()
	
	def Append_Data(self, file):
		df = pd.read_csv(file, sep=None, engine='python')
		drop_cols = ['Row No','Results','Partial Analysis',\
			'ROI Object Count','Completed','Measurement Label',\
			'Snapshot Time Stamp','Water Amount','Weight After',\
			'Weight Before']
		for col in df.columns:
			if re.search('ColorClassAreaRelative|ColorClassName', col):
				drop_cols.append(col)
		for col in drop_cols:
			if col in df.columns:
				df.drop(col, axis=1, inplace=True)
		base = os.path.basename(file)
		df['Filename'] = base[:-4]
		df['Snapshot ID Tag'] = df['Snapshot ID Tag'].astype(str)
		self.data = self.data.append(df, ignore_index=True)
		self.data['Control'] = ' '
	
	def Import_Data(self):
		#Get Items in filebox if not adding additonal files
		if not 'self.additonal_files' in globals():
			self.filenames = []
			for file in list(range(self.File_Selector_Box.count())):
				self.filenames.append(self.File_Selector_Box.itemText(file))
			#import each file into one dataframe, adding filename column 
			self.data = pd.DataFrame()
			for file in self.filenames:
				self.Append_Data(file)
		else:
			for file in self.additional_files:
				self.Append_Data(file)
	
	def Update_Labels(self):
		if self.slpath:
			self.File_Selector_Box.addItems(self.slpath)
			self.Select_File()
					
	def Select_File(self):
		self.Id_List.clear()
		self.Treatments_List.clear()
		current_file = self.File_Selector_Box.currentText()
		current_base = os.path.basename(current_file)
		self.current_base = str(current_base[:-4])
		ids = self.data['Snapshot ID Tag'][self.data.Filename == \
      self.current_base].unique()
		for id in ids:
			self.Id_List.addItem(str(id))
	
	def Get_Id(self):
		self.Id_item = self.Id_List.selectedItems()
		self.Id = []
		for i in self.Id_item:
			self.Id.append(str(self.Id_List.item(self.Id_List.row(i)).text()))
		return self.Id
		
	def Select_Id(self):
		self.Treatments_List.clear()
		self.Reset_Checkboxes()
		self.Get_Id()
		if 'Treatment' in self.data.columns:
			self.Treatments_List.clear()
			treatments_array = []
			for id in self.Id:
				treatment = self.data.Treatment[(self.data['Snapshot ID Tag'] == id) \
					& (self.data.Filename == self.current_base)].unique()
				treatment = treatment.tolist()
				for s in treatment:
					if s not in treatments_array:
						treatments_array.append(s)
				if '' in treatments_array:	
					treatments_array.remove('')
			self.Treatments_List.addItems(treatments_array)
			for treatment in range(len(treatments_array)):
				item = self.Treatments_List.item(treatment)
				item = item.setFlags(
					QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | \
					QtCore.Qt.ItemIsSelectable)
				if self.data.Control[self.data['Treatment'] == self.Treatments_List.item(treatment).text()].unique() == 'Positive':
					self.Treatments_List.item(treatment).setBackground(QtGui.QBrush(QtCore.Qt.green, QtCore.Qt.SolidPattern))
				elif self.data.Control[self.data['Treatment'] == self.Treatments_List.item(treatment).text()].unique() == 'Negative':
					self.Treatments_List.item(treatment).setBackground(QtGui.QBrush(QtCore.Qt.red, QtCore.Qt.SolidPattern))
		else:
			return
			
	def Duplicate_Treatment_Error(self):
		self.Error = QtGui.QErrorMessage(self)
		self.Error.setWindowTitle('Error: Duplicate treatment!')
		self.Error.showMessage('A treatment with that name already exists.')
	
	def Create_Treatment(self):
		self.Treatment_Name = QtGui.QInputDialog.getText(
			self, 'Enter Treatment Name', 'Treatment Name')
		# Check if treatment already exists and raise error
		if self.Treatments_List.findItems(
			self.Treatment_Name[0], QtCore.Qt.MatchFlag(8)):
			self.Duplicate_Treatment_Error()
		# If user clicks "cancel" do nothing
		elif self.Treatment_Name[1] == False:
			return
		else:
			# add and select treatment entered
			self.Treatments_List.addItem(self.Treatment_Name[0])
			new_treatment = self.Treatments_List.findItems(
				self.Treatment_Name[0], QtCore.Qt.MatchFlag(8))
			self.Treatments_List.setCurrentItem(new_treatment[0])
			item = self.Treatments_List.currentItem()
			item = item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled \
													 | QtCore.Qt.ItemIsSelectable)
			#self.Reset_Checkboxes()
	
	def New_Treatment(self):
		# Alert user that treatment will be applied to all ID's
		self.Get_Id()
		if self.File_Selector_Box.count() == 0:
			self.Message = QtGui.QMessageBox(self)
			self.Message.setText('<b>No Files Loaded!</b>')
			self.Message.setWindowTitle('Scanalyzer Analyzer: Warning!')
			self.Message.setInformativeText(
				'You have not loaded any files for analysis. Unless you are saving a' \
				' layout, load files before adding treatments.' )
			self.Message.setStandardButtons(
				QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
			self.Message.setDefaultButton(QtGui.QMessageBox.Ok)
			self.Message.setIcon(QtGui.QMessageBox.Information)
			result = self.Message.exec()
			if result == QtGui.QMessageBox.Ok:
				self.data = pd.DataFrame()
				rows = ['A0', 'B0', 'C0', 'D0']
				plate = pd.Series()
				for row in rows:
					for w in range(1,7):
						series = pd.Series(row + str(w), index=[len(plate)])
						plate = pd.concat([plate, series], ignore_index=True)
				self.data.loc[:,'ROI Label'] = plate
				self.Create_Treatment()
			else: 
				return
		elif self.Id_List.currentItem() == None:
			self.Message = QtGui.QMessageBox(self)
			self.Message.setText('<b>No Snapshot ID selected!</b>')
			self.Message.setWindowTitle('Scanalyzer Analyzer: Warning!')
			self.Message.setInformativeText(
				'You have not selected a Snapshot ID. New treatment class will be ' \
				'applied to all Snapshot ID Tags.')
			self.Message.setStandardButtons(
				QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
			self.Message.setDefaultButton(QtGui.QMessageBox.Ok)
			self.Message.setIcon(QtGui.QMessageBox.Information)
			result = self.Message.exec()
			if result == QtGui.QMessageBox.Ok:
				for i in list(range(self.Id_List.count())):
					self.Id_List.item(i).setSelected(True)
				self.Get_Id()
				self.Create_Treatment()			
			else:
				return
		else:
			self.Create_Treatment()
				
	def Reset_Checkboxes(self):
		#code = "function resetCheckBoxes() {$('.selected').removeClass('selected');};"
		self.frame = self.webView.page().mainFrame()
		self.frame.evaluateJavaScript("resetCheckBoxes()")
	
	def Get_Current_Treatment(self):
		Current_Treatment_Item = self.Treatments_List.currentItem()
		self.Current_Treatment = Current_Treatment_Item.text()
		
	def Select_Treatment(self):
		self.Reset_Checkboxes()
		try:
			self.Get_Current_Treatment()
		except AttributeError:
			return	
		if 'Treatment' in self.data.columns:
			if 'Snapshot ID Tag' in self.data.columns:
				wells = self.data['ROI Label'][(self.data['Snapshot ID Tag'] == \
					self.Id[0]) & (self.data.Treatment == self.Current_Treatment) & \
					(self.data.Filename == self.current_base)].values
				wl = wells.tolist()
				wellssl = []
				for item in wl:
					if item in wellssl:
						del item
					else:
						wellssl.append(str(item))
				code = "var wells = " +json.dumps(wellssl) + "; for (i = 0; i < wells.length; i++) { document.getElementById(wells[i]).className = 'selected';}" 
				print(code)
				self.frame.evaluateJavaScript(code)
			else:
				return
		else: 
			return
			
	def Save_Treatment(self):
		try:
			self.Get_Current_Treatment()
		except AttributeError:
			return
		checked = []
		unchecked = []
		#frame.evaluateJavaScript('saveTreatment()')
		soup = BeautifulSoup(self.frame.toHtml().encode('utf-8'))
		print(soup.find_all(class_ = 'selected'))
		for well in soup.find_all(class_ = 'selected'):
			checked.append(well.get('id'))
		for well in soup.find_all(class_ = None):
			unchecked.append(well.get('id'))
		if 'Treatment' in self.data.columns:
			for id in self.Id:
				self.data.loc[(self.data['Snapshot ID Tag'] == id) & \
					(self.data.Treatment == self.Current_Treatment) & \
					(self.data.Filename == self.current_base), 'Treatment'] = ''
			for check in checked:
				for id in self.Id:
					self.data.loc[(self.data['Snapshot ID Tag'] == id) & \
						(self.data['ROI Label'] == check) & \
						(self.data.Filename == self.current_base), \
						'Treatment'] = self.Current_Treatment
		else:
			self.data['Treatment'] = ''
			for check in checked:
				for id in self.Id:
					self.data.loc[(self.data.Filename == self.current_base) & \
                         (self.data['Snapshot ID Tag'] == id) & \
                         (self.data['ROI Label'] == check),  'Treatment'] = \
                         self.Current_Treatment
		
			
	def Delete_Treatment(self):
		self.Get_Current_Treatment()
		self.Reset_Checkboxes()
		for id in self.Id:
			self.data.loc[(self.data['Filename'] == self.current_base) & \
       (self.data['Snapshot ID Tag'] == id) & (self.data['Treatment'] == \
       self.Current_Treatment[0]), 'Treatment'] = ''
		self.Treatments_List.clear()
		self.Select_Id()
		
	def Edit_Treatment(self):
         self.Treatments_List.editItem(self.Treatments_List.currentItem())

	def Get_Positive_Control(self):
         for id in self.Id:
             self.data.loc[(self.data.Filename == self.current_base) & \
                 (self.data['Snapshot ID Tag'] == id) & \
                 (self.data.Treatment == self.Current_Treatment), 'Control'] = 'Positive'
         item = self.Treatments_List.currentItem()
         item.setBackground(QtGui.QBrush(QtCore.Qt.green, QtCore.Qt.SolidPattern))
         self.Pos_Control_Bool = True
             
	def Get_Negative_Control(self):
         for id in self.Id:
             self.data.loc[(self.data.Filename == self.current_base) & \
                 (self.data['Snapshot ID Tag'] == id) & \
                 (self.data.Treatment == self.Current_Treatment), 'Control'] = 'Negative'
         item = self.Treatments_List.currentItem()
         item.setBackground(QtGui.QBrush(QtCore.Qt.red, QtCore.Qt.SolidPattern))
         self.Neg_Control_Bool = True
        
	def Reset_Plate(self):
		self.Treatments_List.clear()
		self.Reset_Checkboxes()
		del self.data['Treatment']
		
	def Save_Layout(self):
		self.lfpath = r'C:\Scanalyzer Analyzer\layouts.h5'
		#Get Layout name
		layout_name, ok = QtGui.QInputDialog.getText(
			self, 'Enter Layout Name', 'Layout Name')
		if not ok:
			return
		else:
			self.layout_name = layout_name
		# Get Treatments list
		treatments = []
		for i in range(self.Treatments_List.count()):
			treatments_item = self.Treatments_List.item(i)
			treatments.append(treatments_item.text())
		# Get wells for each treatment
		treat_well_pairs = {}
		for treatment in treatments:
			wells = self.data['ROI Label'][(self.data.Filename == \
				self.current_base) & (self.data.Treatment == treatment) & \
				(self.data['Snapshot ID Tag'] == self.Id[0])]
			treat_well_pairs[treatment] = wells.unique()
		layout = pd.DataFrame()
		rows = ['A0', 'B0', 'C0', 'D0', 'E0', 'F0', 'G0', 'H0']
		plate = pd.Series()
		for row in rows:
			for w in range(1,13):
				series = pd.Series(row + str(w), index=[len(plate)])
				plate = pd.concat([plate, series], ignore_index=True)
		layout.loc[:,'Wells'] = plate
		layout['Treatment'] = ''
		for treatment in treat_well_pairs:
			treat_wells = treat_well_pairs[treatment]
			for well in treat_wells:
				#layout['Treatment'][layout.Wells == well] = treatment
				layout.loc[layout.Wells == well, 'Treatment'] = treatment
		if os.path.exists(self.lfpath):
			store = pd.HDFStore(self.lfpath)
			if '/layout/' + self.layout_name in store:
				self.Error = QtGui.QErrorMessage(self)
				self.Error.setWindowTitle('Error: Duplicate layout!')
				self.Error.showMessage('A layout with that name already exists.')
			else:
				group = 'layout/' + self.layout_name
				#layout.to_hdf(self.lfpath, group)
				store[group] = layout
				store.close()
		else:
			if not os.path.exists(self.lfpath[:-10]):
				os.makedirs(self.lfpath[:-10])
			store = pd.HDFStore(self.lfpath)
			store['layout/' + self.layout_name] = layout
			store.close()
	
	def Layout_From_hdf(self):
		layout = self.dialog.Select_Layout()
		treatments = layout['Treatment'].unique()
		treatments = treatments.tolist()
		if '' in treatments:
			treatments.remove('')
		i = 0
		for treatment in treatments:
			self.Treatments_List.addItem(treatment)
			self.Treatments_List.setCurrentItem(self.Treatments_List.item(i))
			i += 1
			
			wells = layout['Wells'][layout.Treatment == treatment]
			wl = wells.tolist()
			wellssl = []
			for item in wl:
				if item in wellssl:
					del item
				else:
					wellssl.append(str(item))
			code = "var wells = " +json.dumps(wellssl) + "; for (i = 0; i < wells.length; i++) { document.getElementById(wells[i]).className = 'selected';}" 
			print(code)
			self.frame.evaluateJavaScript(code)
			self.Save_Treatment()
	
	def Load_Preferences(self):
		self.set_preferences = Preferences(parent=self)
		if self.Set_Negative_Control.isVisible():
			self.set_preferences.Controls_Toggle.setChecked(True)
		self.set_preferences.show()
  
		if self.set_preferences.exec_() == QtGui.QDialog.Accepted:
			if self.set_preferences.Plate_List.currentItem() != None:
				plate = self.set_preferences.Select_Plate()
				self.webView.load(QtCore.QUrl.fromLocalFile(sys._MEIPASS + '/' + plate))
			if self.set_preferences.Controls_Toggle.isChecked():
				self.Set_Negative_Control.show()
				self.Set_Positive_Control.show()
			else:
				self.Set_Negative_Control.hide()
				self.Set_Positive_Control.hide()

	def Load_Layouts(self):
		self.dialog = LayoutLoader(parent=self)
		self.dialog.show()
		
		if self.dialog.exec_() == QtGui.QDialog.Accepted:
			if self.Id_List.currentItem() == None:
				self.Message = QtGui.QMessageBox(self)
				self.Message.setText('<b>No Snapshot ID selected!</b>')
				self.Message.setWindowTitle('Scanalyzer Analyzer: Warning!')
				self.Message.setInformativeText(
					'You have not selected a Snapshot ID. Layout will be applied to' \
					' all Snapshot ID Tags.')
				self.Message.setStandardButtons(
					QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
				self.Message.setDefaultButton(QtGui.QMessageBox.Ok)
				self.Message.setIcon(QtGui.QMessageBox.Information)
				result = self.Message.exec()
				if result == QtGui.QMessageBox.Ok:
					# Select all Snapshot id's and initialize self.Id
					for i in list(range(self.Id_List.count())):
						self.Id_List.item(i).setSelected(True)
					self.Get_Id()	
					# load layout
					self.Layout_From_hdf()
					self.dialog.store.close()
			else:
				self.Get_Id()
				#self.Reset_Plate()
				self.Layout_From_hdf()
				self.dialog.store.close()					
	
	def zfactor(self, x):
		m = x.mean()
		if m == 0:
			z = 1
			return z		
		s = x.std()
		z = 1 - ((3 * s) /  m)
		return z
	
	def Analyze(self):
		zfactorbool = False
		self.aopath = r'C:/Scanalyzer Analyzer/Outputs'
		if not os.path.exists(self.aopath):
			os.mkdir(self.aopath)
		columns = self.data.columns
		for column in columns:
			match = re.search('(?<=_t\(iresult\)).+', column)
			if match:
				self.data.rename(columns={column: match.group(0)}, inplace=True)
		for fname in self.data.Filename.unique():
			df = self.data[self.data.Filename == fname]
			df.loc[:, 'Writer Label'] = df['Writer Label'].astype(object)
			df.loc[:, 'Writer Label'] = df['Writer Label'].str.lower()			
			#Create dataframe of fluorescent data
			fluo = pd.DataFrame(df[df['Writer Label'] == 'fluo'])
			if fluo.size != 0:
				fluo.drop(fluo.columns[pd.isnull(fluo).all()], axis=1, inplace=True)
				fluo.drop('ROI Object Sum Area', axis=1, inplace=True)
				# make list of fluorescent color class names
				fcolor_classes = []
				for column in fluo.columns:
					if 'ColorClassAreaAbsolut' in column:
						fcolor_classes.append(column)
				# Create reversed list of columns for display purposes
				fcolor_classes_rev = fcolor_classes[::-1]
				
				# Calculate zfactors for FLUO, likely will not reach final version
				fzfactors_raw = fluo.groupby(['Snapshot ID Tag', 'Treatment', \
	       'Control']).agg(['mean', 'std'])	
				# Calculate the difference of positive and negative control means across classes
				fzfactors_raw.columns.names = ['class', 'stat']
				fzmeans = fzfactors_raw.xs('mean', level='stat', axis=1)
				fzmeans = fzmeans[(fzmeans.index.get_level_values('Control') != '')]
				fzmeansdiff = fzmeans.groupby(np.arange(len(fzmeans))//2).diff(-1)
				fzmeansdiff = fzmeansdiff.dropna().reset_index()
				fzmeansdiff.drop(['Treatment', 'Control'], axis=1, inplace=True)
				# Calculate the sum of standard dev's of positive and negative controls across classes
				fzstds = fzfactors_raw.xs('std', level='stat', axis=1)
				fzstds = fzstds[(fzstds.index.get_level_values('Control') != '')]
				fzstdssum = fzstds.groupby(np.arange(len(fzstds))//2).sum()
				#create z factor table
				fthreex = 3 * fzstdssum
				fabsolute = fzmeansdiff.iloc[:, 1:].abs()
				fzmeansdiff.iloc[:, 1:] = fabsolute
				fresult = fthreex.divide(fzmeansdiff)
				fresult.iloc[:, 0] = fzmeansdiff.iloc[:, 0]
				fdifference = 1 - fresult.iloc[:, 1:]
				fids = fresult.iloc[:, :1]
				# Create final z factor table
				fzfactor = pd.concat([fids, fdifference], axis=1)
				# slice zfactor table to values from absolute live or absolute dead area
				fzfactorlive = fzfactor.iloc[:, :2]
				fzfactordead = fzfactor.iloc[:, [0,len(fcolor_classes)]]
				fzfactors = pd.concat([fzfactorlive, fzfactordead.iloc[:, 1]], axis=1)
	   
				fpivot = fluo.groupby(['Snapshot ID Tag', 'Treatment']).agg(['mean', 'std'])
				
				'''if self.ZFactor_box.isChecked():
					fmi = pd.MultiIndex.from_product(
						[fcolor_classes_rev, ['mean', 'std', 'zfactor']])
					zfactorbool = True				
				else:'''
				fmi = pd.MultiIndex.from_product([fcolor_classes_rev, ['mean', 'std']])
				
				# Reindex fpivot so that 55-255 color class is first column.
				fpivot = fpivot.reindex_axis(fmi, 1)
				# Create pivot table by treatment
				ftpivot = fluo.groupby(['Treatment']).agg(['mean', 'std', self.zfactor])
				ftpivot = ftpivot.reindex_axis(fmi, 1)
				# Create Table of Averages Only (May be Irrelevant)
				'''fluo_avg = fluo.groupby(
					['Snapshot ID Tag', 'Treatment']).mean()'''
			
			# Create dataframe of visible data
			vis = pd.DataFrame(df[df['Writer Label'] == 'vis'])
			if vis.size != 0:
				vis.drop(vis.columns[pd.isnull(vis).all()], axis=1, inplace=True) 
				
				# make list of visible color class names
				vcolor_classes = []
				for column in vis.columns:
					if 'ColorClassAreaAbsolut' in column:
						vcolor_classes.append(column)
				
				for color in vcolor_classes:
					if 'Agar' in color:
						vcolor_classes.remove(color)
				# Create pivot table of visible color data
				vis2 = vis.copy()
				vis2[vcolor_classes[0]] = \
					vis2['ROI Object Sum Area']/vis2['ROI Area'].max()*100
				if len(vcolor_classes) == 1:
					vpivot = vis2.groupby(['Snapshot ID Tag', 'Treatment'])\
						.agg(['mean', 'std'])
					vtpivot = vis2.groupby(['Treatment']).agg(['mean','std'])
					vis['Percent Area'] = \
						vis['ROI Object Sum Area']/vis['ROI Area'].max()*100
				else:
					vpivot = vis.groupby(['Snapshot ID Tag', 'Treatment'])\
						.agg(['mean', 'std'])
					vtpivot = vis.groupby(['Treatment']).agg(['mean', 'std'])
				try:
					if self.Neg_Control_Bool in globals():
						count = 0
						mil_treat = []
						for l in vpivot.index.get_level_values(0).unique():
	    						count2 = count
	    						for i in vpivot.loc[l].index.tolist():
	    							if vis.loc[(vis['Snapshot ID Tag'] == l) &\
	    								(vis['Treatment'] == i), 'Control']\
									.unique() != 'Negative':
	    								mil_treat.append(i)
	    							else:
	    								mil_treat.insert(count2, i)
	    							count += 1
						vni = pd.MultiIndex.from_arrays(
	    						[vpivot.index.get_level_values(0).tolist(), \
								mil_treat])
						vpivot = vpivot.reindex_axis(vni, 0)
				except AttributeError:
					pass

	# Calculate zfactors for Vis
				vzfactors_raw = vis.groupby(['Snapshot ID Tag', 'Treatment',\
	       'Control']).agg(['mean', 'std'])	
	# Calculate the difference of positive and negative control means across classes
				vzfactors_raw.columns.names = ['class', 'stat']
				vzmeans = vzfactors_raw.xs('mean', level='stat', axis=1)
				vzmeans = vzmeans[(vzmeans.index.get_level_values('Control')\
					!= '')]
				vzmeansdiff = vzmeans.groupby(np.arange(len(vzmeans))//2)\
					.diff(-1)
				vzmeansdiff = vzmeansdiff.dropna().reset_index()
				vzmeansdiff.drop(['Treatment', 'Control'], axis=1, \
					inplace=True)
	# Calculate the sum of standard dev's of positive and negative controls across classes
				vzstds = vzfactors_raw.xs('std', level='stat', axis=1)
				vzstds = vzstds[(vzstds.index.get_level_values('Control') \
					!= '')]
				vzstdssum = vzstds.groupby(np.arange(len(vzstds))//2).sum()
	# create z factor table
				vthreex = 3 * vzstdssum
				vabsolute = vzmeansdiff.iloc[:, 1:].abs()
				vzmeansdiff.iloc[:, 1:] = vabsolute
				vresult = vthreex.divide(vzmeansdiff)
				vresult.iloc[:, 0] = vzmeansdiff.iloc[:, 0]
				vdifference = 1 - vresult.iloc[:, 1:]
				vids = vresult.iloc[:, :1]
	# Create final z factor table
				vzfactor = pd.concat([vids, vdifference], axis=1)
	# slice zfactor table to values from absolute live or absolute dead area
				vzfactorlive = vzfactor.iloc[:, :2]
				vzfactordead = vzfactor.iloc[:, [0,len(vcolor_classes)]]
				vzfactors = pd.concat([vzfactorlive, vzfactordead.iloc[:, 1]], axis=1)
   
	# Create multiindex orded by desired color class order on garph
				if zfactorbool:
					vmi = pd.MultiIndex.from_product(
						[vcolor_classes, ['mean', 'std', 'zfactor']])
				else:
					vmi = pd.MultiIndex.from_product(
						[vcolor_classes, ['mean', 'std']])
				vpivot = vpivot.reindex_axis(vmi, 1)
	# Create pivot table by treatment
				vtpivot = vtpivot.reindex_axis(vmi, 1)
	# Create table of averages (May be irrelevant)		
	# vis_avg = vis.groupby(['Snapshot ID Tag', 'Treatment']).mean()
			
			writer = pd.ExcelWriter(
				self.aopath + r'/{}.xlsx'.format(fname), engine='xlsxwriter')
			if fluo.size != 0:
				fluo.to_excel(writer, 'FLUO', index=False)
				# fzfactors.to_excel(writer, 'FLUO Z-Factors')
				fpivot.to_excel(writer, 'FLUO Treatment by Plate') 
				ftpivot.to_excel(writer, 'FLUO by Treatment') 
			if vis.size != 0:
				vis.to_excel(writer, 'VIS', index=False)
				# vzfactors.to_excel(writer, 'VIS Z-Factors')
				vpivot.to_excel(writer, 'VIS Treatment by Plate')
				vtpivot.to_excel(writer, 'VIS by Treatment')

			workbook = writer.book
			if zfactorbool:
				if fluo.size != 0:
 					fcolumns = ascii_uppercase[2:2 + 3 * len(\
						fcolor_classes):3]
 					ftcolumns = ascii_uppercase[1:1 + 3 * len(\
						fcolor_classes):3]
				if vis.size != 0:
					vcolumns = ascii_uppercase[2:2 + 3 * len(\
						vcolor_classes):3]
					vtcolumns = ascii_uppercase[1:1 + 3 * len(\
						vcolor_classes):3]
			else:
				if fluo.size != 0:	
					fcolumns = ascii_uppercase[2:2 + 2 * len(\
						fcolor_classes):2] 
					ftcolumns = ascii_uppercase[1:1 + 2 * len(\
						fcolor_classes):2]
				if vis.size != 0:
					vcolumns = ascii_uppercase[2:2 + 2 * len(\
						vcolor_classes):2]
					vtcolumns = ascii_uppercase[1:1 + 2 * len(\
						vcolor_classes):2]
    
	# Create FLUO Pivot graph
			if fluo.size != 0:
				chart1 = workbook.add_chart({
					'type': 'column', 'subtype': 'percent_stacked'})
				fpivot_length = len(fpivot) + 3 
				
				i = 0
				fluo_col_names = fpivot.columns.get_level_values(0).unique()
				if len(fcolor_classes) == 2:
					fcolors = ['#006BBC', '#FF0000']
				else:
					fcolors = ['#006BBC', '#95B3D7', '#000000', '#467B1F', \
						'#7EDF4d', '#FFFF00', '#FF0000']
				for column in fcolumns:
					fluo_col_name = re.search('\(.+\)', fluo_col_names[i])
					chart1.add_series({
						'name': fluo_col_name.group(0), \
						'categories': "='FLUO Treatment by Plate'"\
							"!$A$4:$B${}".format(fpivot_length), \
						'values': "='FLUO Treatment by Plate'!${}$4:${}${}"\
							.format(column, column, fpivot_length), \
						'fill': {'color': fcolors[i]}
						})
					i += 1
				chart1.set_size({'width': 850, 'height': 400})
				chart1.set_title({
					'name': "Fluorescent Class Area by Plate", 
					'overlay': False})
				worksheet = writer.sheets['FLUO Treatment by Plate']
				worksheet.insert_chart('C{}'.format(fpivot_length + 2), \
					chart1)

			if vis.size != 0:			
				# Create VIS Treatment by Plate Graph
				if len(vcolor_classes) == 1:
					vcolors = ['#5BA028']
					chart2 = workbook.add_chart({'type': 'column'})
					chart2.set_y_axis({
						'name': 'Percent of Total Area'})
				else:
					chart2 = workbook.add_chart({
						'type': 'column', 'subtype': 'percent_stacked'})
				vpivot_length = len(vpivot) + 3
				vis_col_names = vpivot.columns.get_level_values(0).unique()
				if len(vcolor_classes) == 2:
					vcolors = ['#6A4924', '#5BA028']
				elif len(vcolor_classes) > 2:
					vcolors = ['#B87E3E', '#6A4924', '#5BA028', '#E7E200']
				j = 0
				
				for column in vcolumns:
					vis_col_name = re.search('.+?(?=\.)', vis_col_names[j])
					chart2.add_series({
						'name': vis_col_name.group(0), \
						'categories': "='VIS Treatment by Plate'"\
							"!$A$4:$B${}".format(vpivot_length),
						'values': "='VIS Treatment by Plate'!${}$4:${}${}"\
							.format(column, column, vpivot_length), \
						'fill': {'color': vcolors[j]}
						})
					j += 1
				chart2.set_size({'width': 850, 'height': 400})
				chart2.set_title({
					'name': "Visible Class Area by Plate", 'overlay': False})
				worksheet = writer.sheets['VIS Treatment by Plate']
				worksheet.insert_chart(
					'C{}'.format(vpivot_length + 2), chart2)

			if vis.size != 0:				
				if len(vcolor_classes) == 1:
					vcolors = ['#5BA028']
					chart3 = workbook.add_chart({'type': 'column'})
					chart3.set_y_axis({
						'name': 'Percent of Total Area'})
				else:
					chart3 = workbook.add_chart({
					'type': 'column', 'subtype': 'percent_stacked'})
				vtpivot_length = len(vtpivot) + 3
				
				k = 0
				for column in vtcolumns:
					vis_col_name = re.search('.+?(?=\.)', vis_col_names[k])
					chart3.add_series({
						'name': vis_col_name.group(0), \
						'categories': "='VIS by Treatment'!$A$4:$A${}"\
							.format(vtpivot_length),
						'values': "='VIS by Treatment'!${}$4:${}${}"\
  							.format(column, column, \
						vtpivot_length), \
						'fill': {'color': vcolors[k]}
						})
					k += 1
				chart3.set_size({'width': 550, 'height': 400})
				chart3.set_title({
					'name': "Visible Class Area by Treatment", 
					'overlay': False})
				worksheet = writer.sheets['VIS by Treatment']
				worksheet.insert_chart(
					'C{}'.format(vtpivot_length + 2), chart3)

			if fluo.size != 0:				
				chart4 = workbook.add_chart({
				'type': 'column', 'subtype': 'percent_stacked'})
				ftpivot_length = len(ftpivot) + 3
	
				l = 0
				for column in ftcolumns:
					fluo_col_name = re.search('\(.+\)', fluo_col_names[l])
					chart4.add_series({
						'name': fluo_col_name.group(0), \
						'categories': "='FLUO by Treatment'!$A$4:$A${}"\
							.format(ftpivot_length),
						'values': "='FLUO by Treatment'!${}$4:${}${}"\
							.format(column, column, \
						ftpivot_length), \
						'fill': {'color': fcolors[l]}
						})
					l += 1
				chart4.set_size({'width': 550, 'height': 400})
				chart4.set_title({
					'name': "Fluorescent Class Area by Treatment", 
					'overlay': False})
				worksheet = writer.sheets['FLUO by Treatment']
				worksheet.insert_chart(
					'C{}'.format(ftpivot_length + 2), chart4)
				writer.save()
			
		self.statusBar().showMessage("Analysis is Complete!")
		self.Message = QtGui.QMessageBox(self)
		self.Message.setText('<b>Analysis is Complete!</b>')
		self.Message.setWindowTitle('Scanalyzer Analyzer')
		self.Message.setInformativeText(
			'The analysis is complete and the output file(s) can be found '\
			'in the Outputs folder in C:/Scanalyzer Analyzer.' )
		self.Message.setStandardButtons(QtGui.QMessageBox.Ok)
		self.Message.setDefaultButton(QtGui.QMessageBox.Ok)
		self.Message.setIcon(QtGui.QMessageBox.Information)
		result = self.Message.exec()
		if result == QtGui.QMessageBox.Ok:
			self.File_Selector_Box.clear()
			self.Id_List.clear()
			self.Treatments_List.clear()
			self.Reset_Checkboxes()
		else:
			return
   
class LayoutLoader(QtGui.QDialog, Ui_Layout_Loader):
	def __init__(self, parent=None):
		super(LayoutLoader, self).__init__(parent)
		self.setupUi(self)
		self.lfpath = r'C:\Scanalyzer Analyzer\layouts.h5'
		self.Load_hdf()
		self.Layouts_List.clicked.connect(self.Select_Layout)
		self.Change_Layout_Btn.clicked.connect(self.Change_Path)		
		
	def Load_hdf(self):
		self.store = pd.HDFStore(self.lfpath)
		layouts = self.store.keys()
		for layout in layouts:
			match = re.search('(?<=/layout/)\w+', layout)
			self.Layouts_List.addItem(match.group(0))
	
	def Select_Layout(self):
		if self.Layouts_List.count() < 1:
			return
		else:
			layout = self.Layouts_List.currentItem()
			self.layout = layout.text()
			self.layouts = self.store.keys()
			df = self.store['/layout/' + self.layout]
		return df
	
	def Change_Path(self):
		self.lfpath = QtGui.QFileDialog.getOpenFileNames(
			self, 'Choose Layouts File', '', "hdf (*.h5)")

class Preferences(QtGui.QDialog, Ui_Preferences):
	def __init__(self, parent=None):
		super(Preferences, self).__init__(parent)
		self.setupUi(self)
		self.Get_Plate_Names()
  
	def Get_Plate_Names(self):
		path = sys._MEIPASS + '/'
		files = os.listdir(path)
		for file in files:
			filename, file_ext = os.path.splitext(file)
			if file_ext == '.html':
				self.Plate_List.addItem(filename)

	def Select_Plate(self):
		plate = self.Plate_List.currentItem()
		self.plate = plate.text() + '.html'
		return self.plate

	def Toggle_Control_Selection(self):
		if self.Controls_Toggle.isChecked():
			MainWindow.Set_Negative_Control.show()
			MainWindow.Set_Positive_Control.show()
 
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	frame = MainWindow()
	frame.show()
	app.exec_()
 
