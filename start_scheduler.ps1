#!/usr/bin/env pwsh

Write-Host ""
Write-Host "============================================================================"
Write-Host " CANADIAN HR JOB SEARCH ASSISTANT - SCHEDULER"
Write-Host "============================================================================"
Write-Host ""
Write-Host "Starting automated daily job search scheduler..."
Write-Host "Runs every day at 9:00 AM"
Write-Host ""
Write-Host "Press Ctrl+C to stop"
Write-Host ""
Write-Host "============================================================================"
Write-Host ""

$ProjectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectDir

$venvPath = Join-Path $ProjectDir "venv\Scripts\Activate.ps1"

if (-Not (Test-Path $venvPath)) {
    Write-Host "ERROR: venv not found"
    Read-Host "Press Enter to exit"
    exit 1
}

& $venvPath

pip install schedule

$env:PYTHONPATH = "$ProjectDir\src"
$env:PYTHONPATH = "$ProjectDir\src"
Set-Location $ProjectDir\src
python -m canadian_hr_job_search_assistant.main scheduler
Read-Host "Press Enter to exit"