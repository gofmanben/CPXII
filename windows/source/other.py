#Author Benjamin Gofman

import re, subprocess

hint = 0

out = subprocess.check_output('ipconfig /displaydns', stderr=False)
lines = re.split(r'\r\n', out.decode().strip())
for line in lines:
	if 'Record Name' in line:
		print(line)
		hint = 1
		
if hint:
	print('\nHint: Verify in C:\Windows\System32\drivers\etc\hosts file')

hint = 0
	
out = subprocess.check_output('qwinsta /MODE', stderr=False)
lines = re.split(r'\r\n', out.decode().strip())
for line in lines:
	if 'rdp-tcp' in line:
		print(line)
		hint = 1

if hint:
	print('\nHint: Start -> Run -> control.exe sysdm.cpl,,5 -> Don\'t allow remote connections to this computer')

	
hint = 0