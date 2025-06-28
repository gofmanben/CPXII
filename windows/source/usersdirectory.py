#Author Benjamin Gofman

import re, glob, os, mimetypes

def get_extensions_for_type(general_type):
	for ext in mimetypes.types_map:
		if mimetypes.types_map[ext].split('/')[0] == general_type:
			yield ext

VIDEO = tuple(get_extensions_for_type('video'))
AUDIO = tuple(get_extensions_for_type('audio'))
IMAGE = tuple(get_extensions_for_type('image'))
TEXT = tuple(get_extensions_for_type('text'))
APP = tuple(get_extensions_for_type('application'))

files = []
exts = VIDEO + AUDIO + IMAGE + TEXT +  APP
exclude_dir = r'.*\\AppData\\.*|All Users\\VMware\\.*|All Users\\Microsoft\\.*'

hint=0
os.chdir("C:\\Users")
for f in glob.iglob("**/*", recursive = True):
	if re.match(exclude_dir, f):
		continue
	if any(f.lower().endswith(ext) for ext in exts):
		hint=1
		files.append(f)

print('\n'.join(files))

if hint:
	print('\nHint: Start -> File Explorer -> C:\\Users')