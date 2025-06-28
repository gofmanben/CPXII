@echo off

REM http://woshub.com/reset-local-group-policies-settings-in-windows/

REM https://medium.com/tensult/disable-internet-explorer-enhanced-security-configuration-in-windows-server-2019-a9cf5528be65



powershell -Command "Start-Process 'cmd' -Verb RunAs -ArgumentList '/c gpresult /h C:\GPRreport.html && RD /S /Q %WinDir%\System32\GroupPolicyUsers && RD /S /Q %WinDir%\System32\GroupPolicy && gpupdate /force && exit'"

echo Hint: Start -> Run -> gpedit.msc -> User Configuration -> Administrative Template -> Windows Components -> Internet Explorer
pause
