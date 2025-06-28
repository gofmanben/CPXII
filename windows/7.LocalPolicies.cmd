@echo off

powershell -Command "Start-Process 'cmd' -Verb RunAs -ArgumentList '/c secedit.exe /export /cfg %TEMP%\\secedit.log && exit'"

python\python source\localpolicies.py

del %TEMP%\\secedit.log

pause