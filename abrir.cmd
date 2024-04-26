@echo off
rem Este é um arquivo de lote simples para executar um arquivo Python usando o interpretador Python padrão.

rem Defina o caminho para o interpretador Python padrão.
set PYTHON_PATH=%LOCALAPPDATA%\Programs\Python\Python312\python.exe

rem Verifique se a versão do Python está correta (substitua "XX" pela versão real do Python instalada).

rem Defina o caminho para o arquivo Python que você deseja executar.
set PYTHON_SCRIPT=C:\Users\Josue\Desktop\analisador.py

rem Execute o arquivo Python usando o interpretador Python padrão.
"%PYTHON_PATH%" "%PYTHON_SCRIPT%"

rem Mantenha a janela aberta para que você possa ver a saída antes de fechar.
pause