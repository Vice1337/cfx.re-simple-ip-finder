@echo off
echo ================================
echo CFX.re Finder Setup - Made by v2ce
echo ================================

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed on your system.
    echo Please install Python from https://www.python.org/downloads/ and try again.
    pause
    exit
)

echo Installing required Python libraries...
pip install requests rich

echo Setup complete! You can now run the program using start.bat.
pause
