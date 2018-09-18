# '''rename the files in a folder...'''

import os
path = '/home/firmware/Desktop/helmet/'  #  path of the folder.
files = os.listdir(path)
i = 0

for file in files:
	#str(i) will add file number, if you don't want, remove it.
    os.rename(os.path.join(path, file), os.path.join(path, 'name of file you want'+str(i)+'.jpg'))
    i = i+1
print("All Done !!!, check "+path+".")
