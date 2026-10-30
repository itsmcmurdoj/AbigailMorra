@echo off
title Configure GitHub Access Token
echo ========================================================
echo   Configure GitHub Token for Abigail Morra Portfolio
echo ========================================================
echo.
echo Your repository currently has an active GitHub token configured in .git/config.
echo If you generated a NEW personal access token (starts with ghp_), you can paste it below.
echo.
set /p new_token="Paste your GitHub Personal Access Token (or press Enter to cancel): "
if "%new_token%"=="" (
    echo No changes made.
    goto end
)

git remote set-url origin https://itsmcmurdoj:%new_token%@github.com/itsmcmurdoj/AbigailMorra.git
echo.
echo Updated remote origin! Testing connection...
git ls-remote origin
if %ERRORLEVEL% equ 0 (
    echo.
    echo [SUCCESS] Successfully authenticated with GitHub! You can now push updates.
) else (
    echo.
    echo [ERROR] Authentication failed. Please check that the token is correct and has 'repo' permissions.
)

:end
echo.
pause
