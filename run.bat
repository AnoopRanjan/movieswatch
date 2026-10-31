@echo off
title CinePulse OTT Platform - Python Flask 3.12
echo ======================================================================
echo           CINEPULSE MOVIE STREAMING & CINEMA PLATFORM
echo                     Python 3.12 & Flask
echo ======================================================================
echo.

set "PY_EXE=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
if not exist "%PY_EXE%" (
    set "PY_EXE=python"
)

echo [INFO] Using Python: %PY_EXE%
echo [INFO] Web Server : Flask WSGI
echo [INFO] Local URL  : http://127.0.0.1:5000/
echo.
echo Launching your browser now...
start http://127.0.0.1:5000/

echo.
echo Press Ctrl+C in this window to stop the server when you are done.
echo.

cd /d "%~dp0"
"%PY_EXE%" app.py
