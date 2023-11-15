@echo on
start D:\PentestBox\base\Python3\pythonw ./lxdz.py
pause
::pythonw.exe为后台执行py脚本，不弹出命令框
taskkill /im pythonw.exe /f /t
pause