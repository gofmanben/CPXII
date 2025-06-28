#Author Benjamin Gofman

import re, subprocess

out = subprocess.check_output('wmic SHARE where (Name!="ADMIN$" AND Name!="C$" AND Name!="IPC$") get Name,Path', stderr=False)
lines = re.split(r'\r\n', out.decode().strip())
if len(lines) != 1:
	lines.pop(0)
	print(out.decode().strip())
	print('\nHint: Start -> Run -> compmgmt.msc -> Shared Folders -> Shares -> Right click -> Stop Sharing')
