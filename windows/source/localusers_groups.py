#Author Benjamin Gofman

#wmic path win32_groupuser where (groupcomponent="win32_group.name='administrators',domain='%computername%'")
#wmic USERACCOUNT list full
#net localgroup administrators
#net user ballen

import re, subprocess

admin_users = [line.rstrip('\r\n|\n') for line in open('data\\admins.txt', 'r')]
users = [line.rstrip('\r\n|\n') for line in open('data\\users.txt', 'r')]
newusers = [line.rstrip('\r\n|\n') for line in open('data\\newusers.txt', 'r')]
def_users = ['Administrator', 'DefaultAccount', 'Guest']

all_users = def_users +  admin_users + users + newusers

out = subprocess.check_output('wmic USERACCOUNT get Name', stderr=False)
lines = re.split(r'\r\n|\s+', out.decode().strip())
lines.pop(0)
hint = 0
for user in lines:
	if user not in all_users:
		hint = 1
		print(user, ' - delete user')

for user in newusers:	
	if user not in lines:
		hint = 1
		print(user, ' - add user')
	
if hint:	
	print('\nHint: Start -> Run -> lusrmgr.msc -> Groups -> Administrators\n')

out = subprocess.check_output('net localgroup "Administrators"', stderr=False)
out = re.split(r'.*-----\r\n', out.decode().strip())[1] #delete all lines before Administartor
lines = re.split(r'\r\n', out)
lines.pop() #Delete last line: The command completed successfully.
hint = 0
for user in lines:
	if user != 'Administrator' and user not in admin_users:
		hint = 1
		print(user, ' - delete from "Administrators" group')

if hint:
	print('\nHint: Start -> Run -> lusrmgr.msc -> Users (Do not delete Administrator, DefaultAccount and Guest users\n')
	

def verifyGroup(group, exclude=[]):
	out = subprocess.check_output('net localgroup "%s"' % group, stderr=False)
	out = re.split(r'.*-----\r\n', out.decode().strip())[1] #delete all lines before Administartor
	lines = re.split(r'\r\n', out)
	lines.pop() #Delete last line: The command completed successfully.
	hint = 0
	for user in lines:
		if user in exclude:
			continue
		hint = 1
		print(user, ' - delete from "%s" group' % group)
	if hint:
		print('\nHint: Start -> Run -> lusrmgr.msc -> Users\n')
		
verifyGroup("Access Control Assistance Operators")
verifyGroup("Backup Operators")
verifyGroup("Cryptographic Operators")
verifyGroup("Distributed COM Users")
verifyGroup("Event Log Readers")
verifyGroup("Guests", ["Guest"])
verifyGroup("Hyper-V Administrators")
verifyGroup("IIS_IUSRS", ["NT AUTHORITY\IUSR"])
verifyGroup("Network Configuration Operators")
verifyGroup("Performance Log Users")
verifyGroup("Performance Monitor Users")
verifyGroup("Power Users")
verifyGroup("Remote Desktop Users")
verifyGroup("Remote Management Users")
verifyGroup("Replicator")
verifyGroup("System Managed Accounts Group", ["DefaultAccount"])
verifyGroup("Users", ["NT AUTHORITY\Authenticated Users", "NT AUTHORITY\INTERACTIVE"] + admin_users + users + newusers)
	
out = subprocess.check_output('wmic USERACCOUNT WHERE "Name=\'Administrator\' AND Disabled=1 AND PasswordExpires=0 AND PasswordChangeable=1" GET Name', stderr=False)
lines = re.split(r'\r\n|\s+', out.decode().strip())
if len(lines) != 2:
	print('Administrator - Check "Password never expires" and "Account is disabled"')
	print('\nHint: Start -> Run -> lusrmgr.msc -> Users\n')
	
out = subprocess.check_output('wmic USERACCOUNT WHERE "Name=\'DefaultAccount\' AND Disabled=1 AND PasswordExpires=0 AND PasswordChangeable=1" GET Name', stderr=False)
lines = re.split(r'\r\n|\s+', out.decode().strip())
if len(lines) != 2:
	print('DefaultAccount - Check "Password never expires" and "Account is disabled"')
	print('\nHint: Start -> Run -> lusrmgr.msc -> Users\n')
	
out = subprocess.check_output('wmic USERACCOUNT WHERE "Name=\'Guest\' AND Disabled=1 AND PasswordExpires=0 AND PasswordChangeable=0" GET Name', stderr=False)
lines = re.split(r'\r\n|\s+', out.decode().strip())
if len(lines) != 2:
	print('Guest - Check "User cannot change password", "Password never expires" and "Account is disabled"')
	print('\nHint: Start -> Run -> lusrmgr.msc -> Users\n')
	
out = subprocess.check_output('wmic USERACCOUNT WHERE "Name!=\'Guest\' AND Name!=\'Administrator\' AND Name!=\'DefaultAccount\' AND Disabled=1" GET Name', stderr=False)
lines = re.split(r'\r\n|\s+', out.decode().strip())
if len(lines) > 1:
	lines.pop(0)
	print('Disabled accounts: ', lines)
	print('\nHint: Start -> Run -> lusrmgr.msc -> Users\n')
	
out = subprocess.check_output('wmic USERACCOUNT WHERE "Lockout=1" GET Name', stderr=False)
lines = re.split(r'\r\n|\s+', out.decode().strip())
if len(lines) > 1:
	lines.pop(0)
	print('Locked accounts: ', lines)
	print('\nHint: Start -> Run -> lusrmgr.msc -> Users\n')
	
out = subprocess.check_output('wmic USERACCOUNT WHERE "PasswordExpires=1" GET Name', stderr=False)
lines = re.split(r'\r\n|\s+', out.decode().strip())
if len(lines) > 1:
	lines.pop(0)
	print('Password never expires: (is unchecked) ', lines)
	print('\nHint: Start -> Run -> lusrmgr.msc -> Users\n')
	
out = subprocess.check_output('wmic USERACCOUNT WHERE "Name!=\'Guest\' AND PasswordChangeable=0" GET Name', stderr=False)
lines = re.split(r'\r\n|\s+', out.decode().strip())
if len(lines) > 1:
	lines.pop(0)
	print('User cannot change password: (is checked) ', lines)
	print('\nHint: Start -> Run -> lusrmgr.msc -> Users\n')

