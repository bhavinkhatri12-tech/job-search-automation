# ✅ SETUP CHECKLIST - Just 3 Simple Steps

## Your Setup Checklist

### Step 1: Gmail App Password ⚙️
- [ ] Go to: https://myaccount.google.com/apppasswords
- [ ] Select: **Mail** and **Windows Computer**
- [ ] Copy the 16-character password
- [ ] Example: `xxxx xxxx xxxx xxxx`

### Step 2: Edit .env File 📝
- [ ] Open: `.env` (in project root)
- [ ] Find line: `EMAIL_PASSWORD=your_gmail_app_password_here`
- [ ] Replace with: `EMAIL_PASSWORD=xxxx xxxx xxxx xxxx`
- [ ] Paste your actual Gmail App Password (from Step 1)
- [ ] Save file

### Step 3: Start Scheduler 🚀
- [ ] Find: `start_scheduler.bat` file
- [ ] Copy to: Desktop (optional but recommended)
- [ ] Double-click to start
- [ ] Keep the command window open
- [ ] Done! ✅

---

## Verify It's Working 📧

### Tomorrow Check:
- [ ] Check email inbox at 9:05 AM
- [ ] Look for "Daily Job Search Report"
- [ ] Sender: bhavinkhatri12@gmail.com
- [ ] Contains list of jobs found

### If Email Doesn't Arrive:
1. Check spam folder
2. Check `.env` has correct Gmail App Password
3. Check internet connection
4. See `DEPENDENCY_FIX.md` for troubleshooting

---

## Customization (Optional) 🎨

### Change Time:
- [ ] Edit `.env`
- [ ] Change: `SCHEDULE_TIME=09:00` to your time
- [ ] Example: `SCHEDULE_TIME=14:30` for 2:30 PM
- [ ] Save and restart scheduler

### Change Time Zone:
- [ ] Edit `.env`
- [ ] Change: `TIMEZONE=Canada/Atlantic`
- [ ] Use: Canada/Pacific, Canada/Eastern, etc.

### Change Email:
- [ ] Edit `.env`
- [ ] Change: `EMAIL_RECIPIENT=bhavinkhatri12@gmail.com`
- [ ] Use: any email address

---

## Important Files 📁

- `start_scheduler.bat` - **DOUBLE-CLICK THIS** to start
- `.env` - **EDIT THIS** with Gmail password
- `QUICK_START.md` - Quick reference
- `logs/scheduler.log` - View activity/errors

---

## Daily Schedule 📅

**What happens:**
- Every day at 9:00 AM
- Job search runs automatically
- Email sent with results
- No action needed from you

**To stop:**
- Close the command window
- Or press Ctrl+C

**To resume:**
- Double-click `start_scheduler.bat` again

---

## Keep It Running ⏰

### Best Practice:
1. Start scheduler in morning
2. Keep running all day
3. Close at night (or keep running 24/7)
4. Start again next morning

### Auto-Start on Boot:
1. Press `Win + R`
2. Type: `shell:startup`
3. Copy `start_scheduler.bat` there
4. It will auto-start when you turn on computer

---

## Troubleshooting Quick Reference 🔧

| Problem | Solution |
|---------|----------|
| Window closes immediately | Use `.bat` file (not `.ps1`) |
| Email not arriving | Check Gmail App Password in `.env` |
| "Module not found" error | Run: `venv\Scripts\pip install schedule` |
| Wrong time | Check `.env` SCHEDULE_TIME (use 24-hour format) |
| No internet | Check connection, scheduler needs internet |

---

## Files You Have ✅

```
✅ start_scheduler.bat - USE THIS
✅ start_scheduler.ps1 - Alternative launcher
✅ .env - Configuration (EDIT THIS)
✅ scheduler.py - Scheduling logic
✅ email_utils.py - Email sending
✅ main.py - Updated with scheduler
✅ QUICK_START.md - 5-min guide
✅ SCHEDULER_SETUP.md - Detailed guide
✅ DEPENDENCY_FIX.md - Error help
✅ SETUP_COMPLETE.md - Visual guide
✅ This file - Checklist
```

---

## Done! 🎉

**You have everything you need!**

Next steps:
1. Get Gmail App Password
2. Edit `.env`
3. Double-click `start_scheduler.bat`
4. Check email tomorrow

That's it! Automated job search is ready! 🚀

---

**Questions?**
- See `QUICK_START.md` for 5-minute overview
- See `SCHEDULER_SETUP.md` for detailed help
- See `DEPENDENCY_FIX.md` for troubleshooting
- Check `logs/scheduler.log` for activity

---

## Your Email Will Look Like:

```
From: bhavinkhatri12@gmail.com
To: bhavinkhatri12@gmail.com  
Subject: Daily Job Search Report - 2024-01-15
Time: 9:00 AM

🔍 Daily Job Search Report
✅ 12 Jobs Found Today
✅ 3 Applications Sent
📋 Top Opportunities Listed
✅ Status: Success
⏰ Next Run: Tomorrow at 9:00 AM
```

---

**Ready to automate your job search?**

✅ Yes! Start with Step 1 above.

Good luck! 🚀
