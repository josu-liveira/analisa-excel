@echo off
REM Verificar se a pasta Roaming\pip existe, caso contrário, criar
if not exist "%APPDATA%\pip" mkdir "%APPDATA%\pip"

REM Editar o pip.ini
echo [global] > "%APPDATA%\pip\pip.ini"
echo trusted-host = pypi.python.org pypi.org files.pythonhosted.org >> "%APPDATA%\pip\pip.ini"
echo Arquivo pip.ini editado com sucesso!

REM Exibir pop-up
msg * O diretorio pip foi configurado com sucesso.
