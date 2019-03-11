org = open('S1226-o6-forJNeil', 'r')

newfile = open('obs_OVI.txt', 'w')

newfile.write('Wavelength, Flux\n')

i = 0
for line in org:
	if i > 2:
		data = line.split()
		newfile.write(str(data[0])+', '+str(data[1]+'\n'))
	i = i+1

org.close()
newfile.close()	
