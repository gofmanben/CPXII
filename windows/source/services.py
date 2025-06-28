#Author Benjamin Gofman

import csv, io, subprocess

hint = 0

with open('data\\services.csv', mode='r') as file:
	reader = csv.reader(file)
	source_dict = dict((cols[0],[cols[1],cols[2]]) for cols in reader)

out = subprocess.check_output('wmic SERVICE get DisplayName,StartMode,State  /format:csv', stderr=False)
reader = csv.reader(io.StringIO(out.decode()))
for cols in reader:
	if len(cols) == 4 and cols[0] != 'Node':
		key = cols[1]
		if source_dict.get(key) is None:
			if not key.startswith('CCS Client'):
				print('New Service: ' + key)
				hint = 1
		else:
			if cols[2] != source_dict[key][0]:
				print('StartMode changed: ' + key + '\nORG: ' + source_dict[key][0] + '\nNOW: ' + cols[2])
				hint = 1
			if cols[3] != source_dict[key][1]:
				print('State changed: ' + key + '\nORG: ' + source_dict[key][1] + '\nNOW: ' + cols[3])
				hint = 1
			del source_dict[key]		

if len(source_dict) > 0:
	hint = 1
	for key in source_dict:
		print('Missing: Name=' + key + '\t\tStartMode=' + source_dict[key][0] + '\t\tState=' + source_dict[key][1])
		
if hint:
	print('\nHint: Start -> Run -> services.msc')
