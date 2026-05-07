@echo off
REM ============================================================================
REM Copy Scheduler Files to Desktop
REM ============================================================================

echo.
echo ============================================================================
echo  Copying files to Desktop...
echo ============================================================================
echo.

setlocal enabledelayedexpansion

REM Get Desktop path
set DESKTOP=%USERPROFILE%\Desktop

REM Copy files
echo Copying start_scheduler.bat to Desktop...
copy "start_scheduler.bat" "%DESKTOP%\start_scheduler.bat" >nul
if errorlevel 1 (
    echo ERROR: Could not copy start_scheduler.bat
    pause
    exit /b 1
)
echo OK - start_scheduler.bat copied

echo.
echo Copying QUICK_START.md to Desktop...
copy "QUICK_START.md" "%DESKTOP%\QUICK_START.md" >nul
if errorlevel 1 (
    echo ERROR: Could not copy QUICK_START.md
    pause
    exit /b 1
)
echo OK - QUICK_START.md copied

echo.
echo ============================================================================
echo  SUCCESS! Files copied to Desktop:
echo  - start_scheduler.bat
echo  - QUICK_START.md
echo ============================================================================
echo.
echo You can now delete this script or use it again anytime.
echo.

pause
