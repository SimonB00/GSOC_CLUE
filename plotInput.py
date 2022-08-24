import matplotlib.pyplot as plt
import pandas as pd
import glob


def getFolder(file):
	reversed = file[::-1]
	
	folder = ''
	begin = False
	for char in reversed:
		if char == '/':
			begin = True
		if begin:
			folder += char
	
	return folder[::-1]

fileNotFound = True
file = ''
while fileNotFound:
	file = input('What file do you want to plot? ')
	
	folder = getFolder(file) + '*'
	files = glob.glob(folder)
	if file in files:
		fileNotFound = False
	else:
		print('File not found')

Ndim = int(input('Number of dimensions? '))
df = pd.read_csv(file,header=None)

if Ndim == 2:
	plt.scatter(x=df[0],y=df[1],s=1)
	plt.show()
if Ndim == 3:
	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')
	ax.scatter(df[0],df[1],df[2])

	plt.show()
