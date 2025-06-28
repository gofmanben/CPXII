#Author Benjamin Gofman

import re, subprocess

hint = 0
used = []

out = subprocess.Popen(['powershell.exe', 'Get-ItemProperty -Path HKLM:/SOFTWARE/Microsoft/Windows/CurrentVersion/Uninstall/* | Select-Object DisplayName,DisplayVersion,InstallLocation | Sort-Object DisplayName'], stdout=subprocess.PIPE)
lines = re.split(r'\r\n|\n', out.communicate()[0].decode().strip())
if lines[0].strip().startswith('DisplayName'):
	lines.pop(0)  #DisplayName
	lines.pop(0)  #-----------

	for line in lines:
		if line.strip() == '' or line.startswith('Java') or line.startswith('Microsoft') or line.startswith('VMware'):
			continue
		print('Uninstall(32-bit): ', line)
		used.append(line)
		hint = 1
	
out = subprocess.Popen(['powershell.exe', 'Get-ItemProperty -Path HKLM:/SOFTWARE/Wow6432Node/Microsoft/Windows/CurrentVersion/Uninstall/* | Select-Object DisplayName,DisplayVersion,InstallLocation | Sort-Object DisplayName'], stdout=subprocess.PIPE)
lines = re.split(r'\r\n|\n', out.communicate()[0].decode().strip())
if lines[0].strip().startswith('DisplayName'):
	lines.pop(0)  #DisplayName
	lines.pop(0)  #-----------

	for line in lines:
		if line.strip() == '' or line.startswith('Java') or line.startswith('Microsoft') or line.startswith('VMware'):
			continue
		if line not in used:
			print('Uninstall(64-bit): ', line)
			hint = 1

if not hint:
	out = subprocess.check_output('wmic product get Name,Version', stderr=False)
	lines = re.split(r'\r\n|\n', out.decode().strip())
	lines.pop(0)


	for line in lines:
		if line.startswith('vs') or line.startswith('Java') or line.startswith('Microsoft') or line.startswith('VMware'):
			continue
		print('Uninstall: ', line)
		hint = 1

if hint:
	print('\nHint: Start -> Run -> appwiz.cpl\n')
