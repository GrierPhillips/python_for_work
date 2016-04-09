# convert all .tif files in a directory and sub-directories to .jpg

import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

Tk().withdraw()

folder = askdirectory(initialdir='C:',title='Select folder containing imgages to convert, Thomas.')

for root, dirs, files in os.walk(folder, topdown=False):
		for name in files:
				if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
						if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
						# If a jpeg is *NOT* present, create one from the tiff.
						else:
								outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
								try:
										im = Image.open(os.path.join(root, name))
										im.thumbnail(im.size)
										im.save(outfile, "JPEG", quality=25)
								except Exception:
										print(Exception)
