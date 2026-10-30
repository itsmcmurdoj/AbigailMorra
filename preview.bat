@echo off
title Abigail Morra Portfolio Preview
echo ========================================================
echo   Abigail Morra - Photojournalism Portfolio Preview
echo ========================================================
echo.
echo Starting local web server on port 8080...
echo Opening your browser to: http://localhost:8080
echo.

start http://localhost:8080

where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python -m http.server 8080
    goto end
)

where py >nul 2>nul
if %ERRORLEVEL% equ 0 (
    py -m http.server 8080
    goto end
)

echo Python was not found on your system path.
echo Opening index.html directly in your default browser...
start index.html

:end
pause
