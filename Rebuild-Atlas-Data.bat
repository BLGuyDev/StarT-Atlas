@echo off
cd /d "%~dp0"
title Star Technology Atlas - rebuild data
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\rebuild_data.ps1" %*
echo.
pause
