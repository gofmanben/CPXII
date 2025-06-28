#Author Benjamin Gofman

#https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-gpsb/0b40db09-d95d-40a6-8467-32aedec8140c
#https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/user-rights-assignment
#https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/account-lockout-policy

import configparser, os, csv


name_map ={
	'System Access': 'Account Policies',
	'Event Audit': 'Local Policies -> Audit Policy',
	'Registry Values': 'Local Policies',
	'Privilege Rights': 'Local Policies -> User Rights Assignment'
}

with open('data\\secedit_map.csv', mode='r') as file:
	reader = csv.reader(file)
	source_dict = dict((cols[0].lower(),cols[1]) for cols in reader)

with open('data\\secedit.log', 'r', encoding='utf16') as file:
    org_data = file.read()

with open(os.environ['TEMP'] + '\\secedit.log', 'r', encoding='utf16') as file:
    my_data = file.read()

config1 = configparser.RawConfigParser()
config1.read_string(org_data)

config2 = configparser.RawConfigParser()
config2.read_string(my_data)
hint=0
for sec in config1.sections():
	sec_name = sec
	if name_map.get(sec):
		sec_name = name_map[sec]
	
	if config2[sec] is None:
		print('Section is missing: ' + sec_name)
	else:
		for key in config1[sec]:
			name = key
			if source_dict.get(key):
				name = source_dict[key]
			if config2[sec].get(key) is None:
				hint=1
				print('Section key is missing: ' + sec_name, '->', name)
			elif config1[sec][key] != config2[sec][key]:
				hint=1
				print('Value changed: ' + sec_name, '->', name, '\nLOG: ', config1[sec][key], '\nNOW: ', config2[sec][key])

if hint:
	print('\nHint: Start -> Run -> secpol.msc -> Account or Local Policies')
	
