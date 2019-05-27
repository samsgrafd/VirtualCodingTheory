@Echo On
SetLocal EnableDelayedExpansion
PushD \Program_synthesis
Echo Searching for match profiles.
Set _Found=0
For /F "tokens=* Delims=" %%l In (0,1,2,3,4,5,6,7,8,9) Do (
Echo.%%l|Findstr "0">Nul
If !Errorlevel!==1 (
>>profiles.new Echo 0 1 6     
Set _Found=1
) Else (
>>profiles.new Echo.%%l
)
Echo.%%l|Findstr "0 1 6">Nul
If !Errorlevel!==0 Set _Found=1
)
If %_Found%==0 >>profiles.new Echo.0 1 6     
Rename profiles profile.old
Rename profiles.new profiles

Echo Searching Complete.
Pause
PopD