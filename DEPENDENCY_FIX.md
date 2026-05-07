# 🔧 DEPENDENCY FIX (If Scheduler Doesn't Start)

If you get any module errors when running the scheduler, try these fixes:

---

## Quick Fix (Try This First)

### Step 1: Update Virtual Environment
```bash
cd C:\Users\bhavi\Downloads\CANADIAN_HR_JOB_SEARCH_ASSISTANT
venv\Scripts\activate
pip install --upgrade crewai chromadb
```

### Step 2: Reinstall Dependencies
```bash
pip install -r requirements.txt
```
(If no requirements.txt exists, proceed to next step)

### Step 3: Reinstall All
```bash
pip uninstall crewai crewai-tools -y
pip install "crewai[file-processing,litellm,tools]==1.13.0"
pip install crewai-tools schedule
```

### Step 4: Test Scheduler
```bash
python -m canadian_hr_job_search_assistant.main scheduler
```

---

## If That Doesn't Work

### Full Clean Install
```bash
cd C:\Users\bhavi\Downloads\CANADIAN_HR_JOB_SEARCH_ASSISTANT

# Deactivate venv
deactivate

# Remove old venv
rmdir /s /q venv

# Create fresh venv
python -m venv venv

# Activate
venv\Scripts\activate

# Install everything
pip install --upgrade pip
pip install "crewai[file-processing,litellm,tools]==1.13.0"
pip install crewai-tools schedule

# Test
python -m canadian_hr_job_search_assistant.main scheduler
```

---

## Manual Installation (If Above Doesn't Work)

```bash
# With venv activated:
pip install crewai==1.13.0
pip install crewai-tools
pip install schedule
pip install groq
pip install litellm
```

---

## Check Installation

```bash
# Verify modules are installed
python -c "import crewai; print(f'crewai: {crewai.__version__}')"
python -c "import schedule; print('schedule: OK')"
python -c "import groq; print('groq: OK')"
```

---

## If Still Getting Errors

### Check Your Python Version
```bash
python --version
```
Should be Python 3.10+ and <3.14

### Check Installed Packages
```bash
pip list | findstr crewai
```

### See What's Breaking
```bash
python -m canadian_hr_job_search_assistant.scheduler
```
(Check the actual error message)

---

## Nuclear Option (Last Resort)

Delete entire folder and start fresh:
```bash
# Remove project folder
rmdir /s /q C:\Users\bhavi\Downloads\CANADIAN_HR_JOB_SEARCH_ASSISTANT

# Reinstall from scratch (if you have backup)
```

---

## Common Errors & Fixes

### "ModuleNotFoundError: No module named 'chromadb'"
```bash
pip install chromadb
```

### "ModuleNotFoundError: No module named 'crewai'"
```bash
pip install crewai==1.13.0
```

### "ModuleNotFoundError: No module named 'schedule'"
```bash
pip install schedule
```

### "No module named 'groq'"
```bash
pip install groq
```

---

## Still Having Issues?

1. Try running directly:
```bash
cd C:\Users\bhavi\Downloads\CANADIAN_HR_JOB_SEARCH_ASSISTANT
venv\Scripts\activate
python src/canadian_hr_job_search_assistant/main.py scheduler
```

2. Check error message carefully - it will tell you what's missing

3. Google the error + "crewai" + "python"

4. If nothing works, you might need to:
   - Update Python to latest version
   - Use Python 3.11 specifically if on 3.12

---

## Prevention

Always keep `.venv` and `pyproject.toml` together - they store your dependencies.

If dependencies break, you can usually fix with:
```bash
pip install --upgrade --force-reinstall crewai
```

---

## Still Stuck?

Try this minimal test script to isolate the issue:

Create `test_setup.py` in project root:
```python
#!/usr/bin/env python
import sys
print(f"Python: {sys.version}")

try:
    import crewai
    print("✅ crewai OK")
except Exception as e:
    print(f"❌ crewai ERROR: {e}")

try:
    import schedule
    print("✅ schedule OK")
except Exception as e:
    print(f"❌ schedule ERROR: {e}")

try:
    import groq
    print("✅ groq OK")
except Exception as e:
    print(f"❌ groq ERROR: {e}")

print("\nNow try: python -m canadian_hr_job_search_assistant.main scheduler")
```

Run it:
```bash
python test_setup.py
```

This will show exactly what's broken.

---

## Get Help

If you're really stuck and can't run the scheduler:
1. Take a screenshot of the error
2. Share it with support
3. Include output of: `pip list`
4. Include output of: `python --version`

---

**Most issues can be fixed with:**
```bash
pip install --upgrade --force-reinstall crewai schedule
```
