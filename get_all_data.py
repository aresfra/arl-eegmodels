import h5py
import os
import readhdf5_zhao
import numpy as np

pathlist = []
for root, dirs, files in os.walk("W:\hno\science\TRFinNoise\Rohdaten\Daten\PB_1"):
	for file in files:
		if file.endswith("hdf5"):
			pathlist.append(os.path.join(root, file))


dataset = np.zeros((50400,32,180))	
y_labels = np.zeros((50400,), dtype = int)
for i, filenameh5 in enumerate(pathlist):
	y_labels[i*150:i*150+150] = int(i%7)
	dataset[i*150:i*150+150] = readhdf5_zhao.traverse_datasets(filenameh5)
print("Type and shape of dataset: ", type(dataset), dataset.shape, type(y_labels), y_labels.shape)
