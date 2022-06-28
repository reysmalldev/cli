@echo off
cls
set cmnd=%1
rem Please put where path you saved project in %HERE% , like this : 
rem before = %HERE%\creatorp.py , after: C:\Users\reysmalldev\creatorp.py
python "%HERE%\creatorp.py" %CD% %cmnd%
pause
rem echo -------------- Seu projeto foi Criado -----------------
rem ls