@echo off
cd /d "%~dp0"
title Star Technology Atlas
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\start_atlas.ps1" %*
if errorlevel 1 (
  echo.
  echo Something went wrong. Please read the messages above.
  pause
)
