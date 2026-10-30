@echo off
title Push Updates to Live Portfolio
echo ========================================================
echo   Pushing Abigail Morra Portfolio Updates to GitHub
echo ========================================================
echo.
git status
echo.
set /p commit_msg="Enter a brief note about what changed (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg=Update portfolio from Abigail's Windows PC

echo.
echo Staging files...
git add .

echo Committing: "%commit_msg%"...
git commit -m "%commit_msg%"

echo.
echo Pushing to live GitHub repository...
git push origin main

echo.
echo ========================================================
echo Done! Your live portfolio is updating at:
echo https://itsmcmurdoj.github.io/AbigailMorra/
echo ========================================================
echo.
pause
