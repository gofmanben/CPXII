@echo off


powershell -Command "Start-Process 'cmd' -Verb RunAs -ArgumentList '/c DISM /online /get-features /format:table > %TEMP%\\features.log && exit'"

pause

python\python source\features.py

del %TEMP%\\features.log

pause