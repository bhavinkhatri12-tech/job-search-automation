# ✅ AUTOMATION SETUP - COMPLETE!

## 🎉 Your Automated Job Search is Ready!

Everything has been configured for **daily automated job searches with email reports**.

---

## 📦 What Was Added

### New Files Created:
1. **`start_scheduler.bat`** - Double-click to start daily scheduler
2. **`start_scheduler.ps1`** - PowerShell version of launcher
3. **`QUICK_START.md`** - 5-minute quick start guide
4. **`SCHEDULER_SETUP.md`** - Detailed setup documentation
5. **`src/canadian_hr_job_search_assistant/scheduler.py`** - Scheduling logic
6. **`src/canadian_hr_job_search_assistant/email_utils.py`** - Email sending
7. **`logs/` directory** - For scheduler logs (auto-created)

### Modified Files:
1. **`.env`** - Added email & scheduler configuration
2. **`pyproject.toml`** - Added `schedule` dependency
3. **`src/main.py`** - Added `scheduler` and `run-once` commands

---

## 🚀 QUICK START (Choose One)

### Option A: Desktop Launcher (EASIEST) ⭐
1. **Copy** `start_scheduler.bat` to your Desktop
2. **Double-click it** to start
3. Keep the window open
4. ✅ Done! Runs daily at 9:00 AM

### Option B: Command Line
```bash
cd C:\Users\bhavi\Downloads\CANADIAN_HR_JOB_SEARCH_ASSISTANT
venv\Scripts\activate
python -m canadian_hr_job_search_assistant.main scheduler
```

---

## 📧 SETUP EMAIL NOTIFICATIONS (REQUIRED)

### Step 1: Get Gmail App Password
1. Go to: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Select: **Mail** + **Windows Computer**
3. Copy the 16-character password: `xxxx xxxx xxxx xxxx`

### Step 2: Update .env File
Open `.env` and update:
```
EMAIL_PASSWORD=your_gmail_app_password_here
```
Change to:
```
EMAIL_PASSWORD=xxxx xxxx xxxx xxxx
```

### Step 3: Done!
Save and restart scheduler. You'll now receive daily email reports!

---

## ⏰ CUSTOMIZATION

### Change Run Time
Edit `.env`:
```
SCHEDULE_TIME=09:00
```
Change `09:00` to:
- `08:00` - 8 AM
- `14:30` - 2:30 PM
- `18:00` - 6 PM

### Change Time Zone
Edit `.env`:
```
TIMEZONE=Canada/Atlantic
```
Options:
- `Canada/Pacific` - West Coast
- `Canada/Mountain` - Mountain
- `Canada/Central` - Central
- `Canada/Eastern` - East Coast
- `Canada/Atlantic` - Nova Scotia ✓
- `Canada/Newfoundland` - Newfoundland

### Change Email Recipient
Edit `.env`:
```
EMAIL_RECIPIENT=bhavinkhatri12@gmail.com
```

---

## 📊 WHAT HAPPENS DAILY

**At 9:00 AM (or your configured time):**

1. ✅ Job search automatically runs
2. 📧 Email sent with report containing:
   - Total jobs found
   - Number of applications
   - Top job opportunities
   - Application status
   - Next run schedule

**Email sent to:** bhavinkhatri12@gmail.com (or your configured address)

---

## 🛑 STOPPING THE SCHEDULER

- **Close the command window**, or
- **Press `Ctrl+C`** in the command window

To resume: Double-click `start_scheduler.bat` again

---

## 📋 COMMAND REFERENCE

```bash
# Start daily scheduler
python -m canadian_hr_job_search_assistant.main scheduler

# Run job search once immediately
python -m canadian_hr_job_search_assistant.main run-once

# Run single job search (legacy)
python -m canadian_hr_job_search_assistant.main run

# Train the crew
python -m canadian_hr_job_search_assistant.main train <iterations> <filename>

# Replay from task
python -m canadian_hr_job_search_assistant.main replay <task_id>

# Test the crew
python -m canadian_hr_job_search_assistant.main test <iterations> <model>
```

---

## 🔍 VIEWING LOGS

Check what happened:
```bash
type logs\scheduler.log
```

---

## ❓ TROUBLESHOOTING

### Problem: Command window closes immediately
**Solution:** 
- Right-click `start_scheduler.bat`
- Click "Edit"
- Add `pause` as the last line before closing
- Save and try again

### Problem: "Email_PASSWORD not configured"
**Solution:**
1. Open `.env` file
2. Add your Gmail App Password
3. Restart scheduler

### Problem: "Schedule module not found"
**Solution:**
```bash
venv\Scripts\pip install schedule
```

### Problem: Email not arriving
1. Check spam folder
2. Verify `.env` has correct Gmail password
3. Check internet connection
4. Wait 5 minutes (first run might be slower)

### Problem: "venv not found"
**Solution:**
```bash
python -m venv venv
venv\Scripts\pip install schedule
```

---

## 📱 SYSTEM REQUIREMENTS

- Windows 10/11
- Python 3.10+ (already installed)
- Internet connection
- Gmail account with 2FA enabled
- Virtual environment activated

---

## 🔐 SECURITY NOTES

- Gmail App Password is 16-char temporary password
- Not your regular Gmail password
- Stored only in local `.env` file
- Never share this file

---

## 📞 SUPPORT OPTIONS

1. **Email not sending?** - Check Gmail App Password
2. **Schedule not running?** - Keep command window open
3. **Time wrong?** - Check system clock and `.env` SCHEDULE_TIME
4. **Connection issues?** - Check internet
5. **Check logs:** `logs/scheduler.log`

---

## 🎯 NEXT STEPS

1. ✅ Copy `start_scheduler.bat` to Desktop
2. ✅ Set Gmail App Password in `.env`
3. ✅ Double-click to start scheduler
4. ✅ Check first email (might take a few minutes)
5. ✅ Adjust time if needed
6. ✅ Keep running in background

---

## 💡 TIPS & TRICKS

### Auto-Start on Windows Boot
1. Press `Win + R`
2. Type: `shell:startup`
3. Copy `start_scheduler.bat` there
4. It will auto-start when you boot Windows

### Multiple Schedules
You can run multiple instances at different times:
- Copy `start_scheduler.bat` twice with different `SCHEDULE_TIME` values
- Name them `start_scheduler_morning.bat` and `start_scheduler_evening.bat`

### Keep Updated
Check `logs/scheduler.log` daily to see:
- Jobs found
- Applications sent
- Any errors
- Next scheduled run

---

## 🎊 CONGRATULATIONS!

Your **automated job search assistant** is now fully configured! 

**You will receive daily email reports of job opportunities automatically every day at 9:00 AM.**

Just double-click `start_scheduler.bat` and keep it running!

---

**Questions? Check:**
- `QUICK_START.md` - 5-minute setup
- `SCHEDULER_SETUP.md` - Detailed guide
- `logs/scheduler.log` - Error messages
- `.env` - Configuration file

Happy job hunting! 🚀
