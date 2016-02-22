import numpy as np
import pandas as pd
from PIL import Image
from scipy import ndimage
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
Tk().withdraw() #don't want a full GUI, so keep root window from appearing

# Create list of plate well names for labelling later
plate_layout = []
rows = ['A', 'B', 'C', 'D']
for i in range(1, 7):
	for letter in rows:
		plate_layout.append(letter + i) 

# Create a list of strings containing the filenames
files_to_analyze = askopenfilenames(initialdir='C:',title='Select picture files to analyze')

for fname in files_to_analyze:

	# Open image and create an array of original. Convert image to grayscale and create black and white array. 
	img = Image.open(fname)
	img_array = np.asarray(img).copy()
	gray = img.convert('L')
	bw = np.asarray(gray).copy()
	# Fix values for any color other than white to black
	bw[bw<250] = 0
	bw[bw>250] = 255
	# Create mask of image using top left corner pixel as default background
	bg = bw[0,0]
	mask = bw != bg

	# Use ndimage.label to label objects, then find_objects to pull location data
	labels, num_wells = ndimage.measurements.label(mask)
	slices = ndimage.find_objects(labels)

	# Sort the slices according to x,y coordinates
	'''This is accomplished by passing the slice data for each row of the plate through a y sort and compiling a list'''
	def sort_by_x():
		return lambda x: x[1].start	
	i = 0
	sort_slices =[]
	for j in range(6,30,6):
		sort_slices.extend(sorted(slices[i:j], key=sort_by_x()))
		i += 6

	'''# Plot original image, black and white masked image, and labeled objects image.
	fig, ax = plt.subplots()
	ax.imshow(img)
	ax.set_title('Original Image')

	fig, ax = plt.subplots()
	ax.imshow(bw)
	ax.set_title('Black and White Masked Image')

	fig, ax = plt.subplots()
	ax.imshow(labels)
	ax.set_title('Labeled Objects')'''

	# Plot all 24 wells as individual objects.
	fig, axes = plt.subplots(ncols=6, nrows=4, figsize=(14,9))
	i = 0
	for ax, slice in zip(axes.flat, sort_slices):
		ax.imshow(img_array[slice], vmin=0, vmax=num_wells)
		tuple = '{layout}:\nymin:{0.start}, ymax:{0.stop}\nxmin:{1.start}, xmax:{1.stop}'
		ax.set_title(tuple.format(layout=plate_layout[i], *slice), fontsize=10, y=1.05)
		img_save = Image.fromarray(img_array[slice])
		img_save.save(r'{}{}.png'.format(fname[:-4], plate_layout[i]))
		i += 1
	fig.suptitle('Individual Wells', fontsize=24)
	fig.tight_layout(pad=4, h_pad=.5, w_pad=.25)
	fig.savefig(r'{}_Individual_Objects_Data.png'.format(fname[:-4]))

	# plt.show()



