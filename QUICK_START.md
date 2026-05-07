# ⚡ Quick Start - 5 Minutes Setup

## Your Files Are Ready! 📦

You now have everything to run automated daily job searches. Here's how:

---

## 🎯 3-Step Setup (5 Minutes)

### Step 1: Get Gmail App Password (2 min)
1. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Login if needed
3. Select: **Mail** + **Windows Computer**
4. Copy the 16-character password

### Step 2: Update .env File (1 min)
Open `.env` in the project folder and change:
```
EMAIL_PASSWORD=your_gmail_app_password_here
```
to:
```
EMAIL_PASSWORD=xxxx xxxx xxxx xxxx
```
(Replace with your actual password)

### Step 3: Start Scheduler (1 min)
**Double-click this file to start:**
- 👉 `start_scheduler.bat` (on Desktop or in project folder)

Done! ✅ Your job search runs daily at 9:00 AM

---

## 📧 What Happens

- **Every Day at 9:00 AM** - Job search runs automatically
- **Email Sent** - You get a report with found jobs
- **Keep Running** - Leave the command window open in background

---

## 🛑 Stop or Pause

Close the command window to stop the scheduler.

---

## 🔧 Change Time (Optional)

Want it to run at a different time? Edit `.env`:

Change `SCHEDULE_TIME=09:00` to whatever you want:
- `08:00` - 8 AM
- `14:30` - 2:30 PM
- `18:00` - 6 PM

Then restart the scheduler.

---

## ❓ Issues?

**Command window closes immediately?**
- Right-click `start_scheduler.bat` → Edit
- Add `pause` at the end
- Save and try again

**Email not arriving?**
- Make sure you used Gmail App Password (not your regular password)
- Check spam folder
- Check internet connection

**Need more help?**
- See `SCHEDULER_SETUP.md` for detailed guide
- Check `logs/scheduler.log` for error messages

---

## 📱 You Have Two Launcher Files

1. **start_scheduler.bat** - For Command Prompt (Easiest)
2. **start_scheduler.ps1** - For PowerShell

Use whichever you prefer!

---

**That's it! Your automated job search is ready.** 🚀

Keep the scheduler running and check your email daily for opportunities!
