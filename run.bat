@echo off
REM Check if the virtual environment exists
if not exist win_venv (
    echo Error: Virtual environment not found. Please ensure the venv directory is included.
    exit /b 1
)

REM Activate the virtual environment
call win_venv\Scripts\activate

REM Run the game using pythonw to suppress the console
win_venv\Scripts\pythonw.exe main.py

REM Deactivate the virtual environment (optional, if you want to clean up)
deactivate