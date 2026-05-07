# 🔍 Canadian HR Job Search Assistant - Automated Setup Guide

## Overview
Your job search assistant is now configured to run **automatically every day at 9:00 AM** with email notifications.

---

## ⚙️ SETUP REQUIRED: Gmail App Password

To enable email reports, you need to create a **Gmail App Password**:

### Step 1: Enable 2-Factor Authentication
1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Click "Security" in the left menu
3. Scroll to "2-Step Verification" and enable it (if not already enabled)

### Step 2: Generate App Password
1. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Select **Mail** and **Windows Computer**
3. Google will generate a 16-character password like: `xxxx xxxx xxxx xxxx`
4. Copy this password

### Step 3: Update .env File
1. Open the `.env` file in the project root
2. Replace `your_gmail_app_password_here` with your 16-character password:
   ```
   EMAIL_PASSWORD=xxxx xxxx xxxx xxxx
   ```
3. Save the file

---

## 🚀 How to Run the Scheduler

### Option 1: Desktop Launcher (Easiest) ⭐
1. **Copy** `start_scheduler.bat` to your Desktop
2. **Double-click** the file to start the scheduler
3. A command window will appear showing status
4. Keep it running in the background

**To Stop:** Close the command window or press `Ctrl+C`

### Option 2: PowerShell Launcher
1. **Copy** `start_scheduler.ps1` to your Desktop
2. **Right-click** → "Run with PowerShell"
3. If you get an execution policy error, run PowerShell as Admin and type:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
4. Then try again

### Option 3: Command Line
From the project directory:
```bash
python -m canadian_hr_job_search_assistant.main scheduler
```

---

## ⏰ Configuration

### Change Schedule Time
1. Open `.env` file
2. Change `SCHEDULE_TIME=09:00` to your preferred time (24-hour format)
   - Example: `SCHEDULE_TIME=14:30` for 2:30 PM
3. Save and restart the scheduler

### Change Time Zone
1. Open `.env` file
2. Update `TIMEZONE=Canada/Atlantic` to your time zone:
   - `Canada/Pacific` - West Coast
   - `Canada/Mountain` - Mountain Time
   - `Canada/Central` - Central Time
   - `Canada/Eastern` - East Coast
   - `Canada/Atlantic` - Atlantic Time (Nova Scotia)
   - `Canada/Newfoundland` - Newfoundland

### Change Email Recipient
1. Open `.env` file
2. Change `EMAIL_RECIPIENT` to receive reports at a different email

---

## 📧 What You'll Receive

### Daily Email Report
- **Time:** 9:00 AM (or your configured time)
- **To:** bhavinkhatri12@gmail.com
- **Contains:**
  - Number of jobs found
  - Number of applications sent
  - List of top job opportunities
  - Application status
  - Next scheduled run time

---

## 📋 Command Reference

### Run Once Immediately
```bash
python -m canadian_hr_job_search_assistant.main run-once
```

### Start Scheduler
```bash
python -m canadian_hr_job_search_assistant.main scheduler
```

### Run Single Search
```bash
python -m canadian_hr_job_search_assistant.main run
```

---

## 🛠️ Troubleshooting

### Email not sending?
1. Check `.env` file - ensure `EMAIL_PASSWORD` is set
2. Verify it's a Gmail App Password (not your regular password)
3. Check internet connection
4. Check `logs/scheduler.log` for errors

### Command window closes immediately?
1. Use the `.bat` file instead (keeps window open)
2. Or run from PowerShell/Command Prompt directly

### Schedule not running?
1. Keep the command window open in background
2. Check that time is in 24-hour format (e.g., `09:00` not `9:00 AM`)
3. Verify system clock is correct
4. Check `logs/scheduler.log` for error messages

### "Python not found" error?
1. Ensure virtual environment is activated
2. Run: `venv\Scripts\activate.bat` first
3. Then: `python -m canadian_hr_job_search_assistant.main scheduler`

---

## 📁 Files Created/Modified

### New Files:
- `start_scheduler.bat` - Desktop launcher (Batch)
- `start_scheduler.ps1` - Desktop launcher (PowerShell)
- `src/canadian_hr_job_search_assistant/scheduler.py` - Scheduling logic
- `src/canadian_hr_job_search_assistant/email_utils.py` - Email functionality
- `logs/scheduler.log` - Execution logs (auto-created)

### Modified Files:
- `.env` - Added email and scheduler configuration
- `pyproject.toml` - Added schedule dependency
- `src/canadian_hr_job_search_assistant/main.py` - Added scheduler commands

---

## 🔄 Auto-Start (Optional)

### Windows Task Scheduler
1. Press `Win + R`, type `taskschd.msc`, press Enter
2. Click "Create Basic Task"
3. Set trigger to "Daily" at 9:00 AM
4. Set action: Start program
   - Program: `C:\path\to\venv\Scripts\pythonw.exe`
   - Arguments: `-m canadian_hr_job_search_assistant.main scheduler`
   - Start in: `C:\path\to\CANADIAN_HR_JOB_SEARCH_ASSISTANT`

---

## 📊 Viewing Logs

Check execution logs:
```bash
type logs\scheduler.log
```

---

## ✅ Quick Start Checklist

- [ ] Set Gmail App Password in `.env`
- [ ] Copy `start_scheduler.bat` to Desktop
- [ ] Double-click to start scheduler
- [ ] Check first email report in inbox
- [ ] Adjust `SCHEDULE_TIME` if needed
- [ ] Keep scheduler running in background

---

## 📞 Support

For issues, check:
1. `.env` file configuration
2. `logs/scheduler.log` file
3. Gmail App Password setup
4. Internet connection
5. System time/timezone

---

**Your job search is now automated! Sit back and receive daily reports of opportunities.** 🚀
