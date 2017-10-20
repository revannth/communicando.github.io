import os
f = open('names.txt', 'w')

for root, dirs, files in os.walk('./'):
	for newname in files:
		filename = os.path.join(newname)
		newstring = "ccd_snr/" + filename + '\n'
		f.write(newstring)
