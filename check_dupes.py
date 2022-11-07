import numpy as np
import glob, json

files1 = glob.glob('kne-internal/GRB*')
files2 = glob.glob('kne-2000-2029/*')

for f1 in files1:
	for f2 in files2:
		match = False
		if (str(f1.split('/')[-1][:-5]) == str(f2.split('/')[-1][:-5])): match = True
		if match:
			file1 = open(f1)
			file2 = open(f2)
			data1 = json.load(file1, encoding="UTF-8")
			data2 = json.load(file2, encoding="UTF-8")
			data1 = data1[f1.split('/')[-1].split('.')[0]]['photometry']
			data2 = data2[f2.split('/')[-1].split('.')[0]]['photometry']
			print(len(data1), len(data2))
				
