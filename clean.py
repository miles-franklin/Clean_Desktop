# This script moves image files from the Desktop to a 
# Screen_Shots foler.

import os
import shutil

path = os.path.expanduser("~")
path = os.path.join(path, "Desktop")

files = os.listdir(path)

# Filter out folders 
files = [f for f in files if os.path.isfile(os.path.join(path, f))]
# Filter for desired file extentions
files = [f for f in files if ".png" in f 
						  or ".mov" in f 
						  or ".jpg" in f 
						  or ".jpeg" in f]


for f in files:
	print(f)
	print(end="\tMoving file...\t")
	
	src = os.path.join(path, f)
	dst = os.path.join(path, "Screen_Shots", f)
	os.rename(src, dst)

	print("Done")

