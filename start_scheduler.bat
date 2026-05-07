@echo off
REM ============================================================================
REM Canadian HR Job Search Assistant - Desktop Launcher
REM Automated Daily Job Search with Email Reports
REM ============================================================================

setlocal enabledelayedexpansion

REM Get the project directory (folder of this script)
cd /d "%~dp0"

REM Set PYTHONPATH to include src for module resolution
set PYTHONPATH=%CD%\src

REM Set schedule time and email recipient as environment variables
set SCHEDULE_TIME=09:00
set EMAIL_RECIPIENT=bhavinkhatri12@gmail.com


REM Activate virtual environment (try venv, then .venv, else create venv)
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else if exist .venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
) else (
    echo Virtual environment not found. Creating one now...
    python -m venv venv
    if exist venv\Scripts\activate.bat (
        call venv\Scripts\activate.bat
    ) else (
        echo Error: Failed to create or activate virtual environment
        pause
        exit /b 1
    )
)

REM Check if schedule module is installed
python -c "import schedule" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
)

REM Run the scheduler (auto daily at 9am)
cd src
python -m canadian_hr_job_search_assistant.main scheduler

pause
