@echo off
REM Check if the virtual environment already exists
if exist venv (
    echo Virtual environment found.
) else (
    REM Create a new virtual environment
    echo Creating a virtual environment...
    python -m venv venv

    REM Check if venv creation was successful
    if %ERRORLEVEL% neq 0 (
        echo Failed to create virtual environment. Ensure Python is installed and available in PATH.
        exit /b 1
    )
)

REM Activate the virtual environment
call venv\Scripts\activate

REM Ensure pip is up to date
echo Upgrading pip to the latest version...
python -m pip install --upgrade pip

REM Install the required version of pygame
echo Installing Pygame 2.6.0...
pip install pygame==2.6.0

REM Check if pygame installation was successful
if %ERRORLEVEL% neq 0 (
    echo Failed to install Pygame. Please check your internet connection or pip configuration.
    exit /b 1
)

REM Run the game
echo Running the game...
./python.exe main.py

REM Deactivate the virtual environment
deactivate
