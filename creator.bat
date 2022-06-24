@echo off
set cmnd=%1
cls
python "%CD%\creatorp.py" %CD% %cmnd%
pause
rem echo -------------- Seu projeto foi Criado -----------------
rem ls