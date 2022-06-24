@echo off
set cmnd=%1
cls
python "C:\workspace\python\cli\creatorp.py" %CD% %cmnd%
pause
rem echo -------------- Seu projeto foi Criado -----------------
rem ls