#Author Benjamin Gofman

import os, glob

hint=0

programfiles = ['Common Files', 'desktop.ini', 'Internet Explorer', 'Java', 'Mozilla Firefox', 'Uninstall Information', 'VMware', 
	'Windows Defender', 'Windows Mail', 'Windows Media Player', 'Windows Multimedia Platform', 'Windows NT', 'Windows Photo Viewer',
	'Windows Portable Devices', 'Windows Sidebar', 'WindowsApps', 'WindowsPowerShell']

programfiles86 = ['Common Files', 'desktop.ini', 'Internet Explorer', 'Microsoft.NET', 'Notepad++', 'Windows Defender', 'Windows Mail', 
	'Windows Media Player', 'Windows Multimedia Platform', 'Windows NT', 'Windows Photo Viewer', 'Windows Portable Devices', 'Windows Sidebar', 'WindowsPowerShell']
	
programdata = ['Application Data', 'Comms', 'Desktop', 'Documents', 'Microsoft', 'ntuser.pol', 'Start Menu', 'Sun', 'Templates', 'USOPrivate', 'USOShared', 'VMware']
	
list = os.listdir("C:\\Program Files")
for dir in list:
	if dir not in programfiles:
		hint = 1
		print("C:\\Program Files\\" + dir)
	
if os.path.exists("C:\\Program Files (x86)"):
	list = os.listdir("C:\\Program Files (x86)")
	for dir in list:
		if dir not in programfiles86:
			hint = 1
			print("C:\\Program Files (x86)\\" + dir)

if os.path.exists("C:\\ProgramData"):
	list = os.listdir("C:\\ProgramData")
	for dir in list:
		if dir not in programdata:
			hint = 1
			print("C:\\ProgramData\\" + dir)
		
if hint:
	print('\nHint: Start -> File Explorer')
