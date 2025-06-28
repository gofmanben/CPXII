#Author Benjamin Gofman

import subprocess, csv, io

with open('data\\tasks.csv', mode='r') as file:
	reader = csv.reader(file)
	source_dict = dict((cols[0],cols[2]) for cols in reader)
	
	
out = subprocess.check_output('schtasks.exe /query /fo csv', stderr=False)
reader = csv.reader(io.StringIO(out.decode()))
my_dict = dict((cols[0],cols[2]) for cols in reader)

del my_dict['TaskName']

hint=0
for key in my_dict:
	if source_dict.get(key) is None:
		if not key.startswith('\\User_Feed_Synchronization'):
			print('New Task: ' + key)
			hint = 1
	elif my_dict[key] != source_dict[key]:
		print('Value changed: ' + key + '\nORG: ' + source_dict[key] + '\nNOW: ' + my_dict[key])
		del source_dict[key]
		hint = 1
	else:
		del source_dict[key]
		

if len(source_dict) > 0:
	hint = 1
	for key in source_dict:
		if not key.startswith('\\User_Feed_Synchronization'):
			print('Missing task name and value: ' + key + '=' + source_dict[key])
		

if hint:
	print('\nHint: Start -> Run -> taskschd.msc -> Task Scheduler Library -> Miscrosoft -> Windows')
