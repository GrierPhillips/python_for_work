from PIL import Image, ImageFilter
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import numpy as np
import pandas as pd
import math

Tk().withdraw()

class Analysis(object):
	def __init__(self, file):
		self.file = file
		self.img = Image.open(file)
		self.find_segments()	
	
	def find_segments(self):
		# Find and return segments where image fits for np or pd manipulation
		width, height = self.img.size
		r = height/2
		# Python math works in radians so convert angle to radians
		angle = math.radians(45)
		# Find y where 45deg intersects the edge and set lower and upper values
		y = int(math.floor(r * math.sin(angle)))
		self.upper_bound = math.floor(r - y)
		self.lower_bound = height - self.upper_bound		
		
	def find_area(self):
	# Convert image to greyscale, then adjust to b/w
		#img = Image.open(file)
		gray = self.img.convert('L')
		bw = np.asarray(gray).copy()
		bw = np.where(bw>250, np.nan, 0) 	# Fix values for any color other than white to black
		# Create a copy of the b/w numpy array for processing by rows first
		bw_area = bw.copy()
		
		# Adjust the rows between upper bound and lower bound where there are duplicate vertical pixels of border
		size = list(range(self.upper_bound, self.lower_bound))
		for row in size:
			index = np.where(bw_area[row]==0)
			bw_area[row][index[0][0]] = np.nan
			bw_area[row][index[0][-1]] = np.nan

		# Identify the x coordinates for the y range remaining to be adjusted
		xvals_ymin = np.where(bw_area[self.upper_bound-1]==0)
		xvals_ymax = np.where(bw_area[self.lower_bound+1]==0)
		xl_ymin = xvals_ymin[0][0]
		xr_ymin = xvals_ymin[0][-1]
		xl_ymax = xvals_ymax[0][0]
		xr_ymax = xvals_ymax[0][-1]
		
		# Convert bw_area to DataFrame to process columns
		bw_areadf = pd.DataFrame(np.array(bw_area))
		bw_areadf = bw_areadf.replace(255, np.nan)
		# Pass columns into remaining unprocessed regions of image
		top = list(range(xl_ymin, xr_ymin + 1))
		bottom = list(range(xl_ymax, xr_ymax + 1))
		for col in top:		
			bw_areadf.ix[bw_areadf[col].first_valid_index(), col] = np.nan
		for col in bottom:	
			bw_areadf.ix[bw_areadf[col].last_valid_index(), col] = np.nan	
		
		area = bw_areadf.count().sum()
		print(area)
		# If needed use below line to output dataframe as excel
		# area.to_excel(r'{}.xlsx'.format(fname[:-4]))
		
		return area
		
if __name__ == "__main__":
	files = askopenfilenames(initialdir='C:',title='Select picture files to analyze')
	for file in files:	
		output = Analysis(file)
		print(output)
		area = output.find_area()
		print(area)