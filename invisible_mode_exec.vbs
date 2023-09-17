Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\Batch Files\syncfiles.bat(location of the bat file)" & Chr(34), 0
Set WshShell = Nothing