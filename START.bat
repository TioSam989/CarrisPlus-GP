@echo off
echo ========================================
echo   CarrisPlus - Starting Services
echo ========================================
echo.
echo Starting Docker containers...
echo This may take a few minutes on first run.
echo.

docker-compose up --build

pause
