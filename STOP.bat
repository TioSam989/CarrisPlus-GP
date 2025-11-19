@echo off
echo ========================================
echo   CarrisPlus - Stopping Services
echo ========================================
echo.
echo Stopping Docker containers...
echo.

docker-compose down

echo.
echo Services stopped!
pause
