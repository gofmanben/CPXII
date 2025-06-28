#Author Benjamin Gofman

import re, subprocess

hint = 0
try:
	out = subprocess.check_output('netsh advfirewall show allprofiles state', stderr=False)

	lines = re.split(r'\r\n|\n', out.decode().strip())
	index = 0
	while index < len(lines):
		line = lines[index]
		if line.startswith('Domain Profile Settings:') or \
			line.startswith('Private Profile Settings:') or \
			line.startswith('Public Profile Settings:'):
			index += 2
			state = re.sub('\s+', ' ', lines[index])
			if state != 'State ON':
				hint = 1
				print(line, state)
		index += 1
		
		
	out = subprocess.check_output('netsh advfirewall show allprofiles firewallpolicy', stderr=False)
	lines = re.split(r'\r\n|\n', out.decode().strip())
	index = 0
	while index < len(lines):
		line = lines[index]
		if line.startswith('Domain Profile Settings:') or \
			line.startswith('Private Profile Settings:') or \
			line.startswith('Public Profile Settings:'):
			index += 2
			state = re.sub('\s+', ' ', lines[index])
			if state != 'Firewall Policy BlockInbound,AllowOutbound':
				hint = 1
				print(line, state)
		index += 1

	if hint:
		print('\nHint: Start -> Run -> control firewall.cpl')
except:
  print('"Windows Firewall" service is disabled. You must enable first')
