@echo off

echo https://www.shouldiremoveit.com
echo -------------------------------------------------------
wmic startup get caption,command

echo Hint: Start -> Run -> msconfig -> Startup tab

echo -------------------------------------------------------
echo or seach next keys in regedit
echo HKU - HKEY_USERS
echo HKLM - HKEY_LOCAL_MACHINE

wmic startup get caption,location
echo -------------------------------------------------------

pause