setlocal EnableDelayedExpansion 

for /F "usebackq delims=" %%a in ("%log_dir%\numbers.txt") do @echo "%%a" + "\r\n +"
