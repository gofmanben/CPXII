#Author Benjamin Gofman

import re, os

hint = 0
org_dic = {}
cur_dic = {}

with open('data\\features.log', 'r') as file:
    lines = re.split(r'\r\n|\n', file.read())
for line in lines:
	pair = re.split('\|', re.sub(r'\t+|\s+', '', line))
	if len(pair) == 2:
		org_dic[pair[0]] = pair[1]

with open(os.environ['TEMP'] + '\\features.log', 'r') as file:
    lines = re.split(r'\r\n|\n', file.read())
for line in lines:
	pair = re.split('\|', re.sub(r'\t+|\s+', '', line))
	if len(pair) == 2:
		cur_dic[pair[0]] = pair[1]

for name in cur_dic:
	if org_dic.get(name) and cur_dic[name] != org_dic[name]:
		hint=1
		print('Feature Name: ' + name, '\nLOG: ', org_dic[name], '\nNOW: ', cur_dic[name])
		

if hint:
	print('\nHint: Start -> Run -> optionalfeatures\n\nor\n')
	print('Get List of features:  DISM /Online /Get-Features /Format:table')
	print('Disable feature:       DISM /Online /Disable-Feature /FeatureName:{FEATURE_NAME}')
	print('Enable feature:        DISM /Online /Enable-Feature /FeatureName:{FEATURE_NAME}\n')

