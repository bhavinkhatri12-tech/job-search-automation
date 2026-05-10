#!/usr/bin/env python
"""Daily job search scheduler module."""

import schedule
import time
import os
import re
from datetime import datetime
from pathlib import Path
from canadian_hr_job_search_assistant.crew import CanadianHrJobSearchAssistantCrew
from canadian_hr_job_search_assistant.email_utils import send_email_report, create_crew_output_report

MAX_RATE_LIMIT_RETRIES = 6


def kickoff_with_rate_limit_retry(inputs):
    """Run the crew and wait/retry when Groq returns a TPM rate limit."""
    for attempt in range(1, MAX_RATE_LIMIT_RETRIES + 1):
        try:
            return CanadianHrJobSearchAssistantCrew().crew().kickoff(inputs=inputs)
        except Exception as e:
            message = str(e)
            if "rate_limit" not in message.lower() and "ratelimit" not in message.lower():
                raise

            match = re.search(r"try again in ([0-9.]+)s", message, re.IGNORECASE)
            suggested_wait = float(match.group(1)) if match else 0
            wait_seconds = max(suggested_wait + 10, 75)

            if attempt == MAX_RATE_LIMIT_RETRIES:
                raise

            log_file(
                f"Rate limit hit; waiting {wait_seconds:.1f}s before retry "
                f"{attempt + 1}/{MAX_RATE_LIMIT_RETRIES}"
            )
            print(f"Rate limit hit. Waiting {wait_seconds:.1f}s before retry...")
            time.sleep(wait_seconds)


def run_job_search():
    """Execute job search crew with logging."""
    print("\n" + "="*80)
    print(f"🚀 Starting Job Search at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    inputs = {
        'job_search_domain': 'Canadian HR',
        'candidate_profile': 'Bhavin Khatri, HR/Admin/Recruitment Professional with 12+ years experience based in Nova Scotia, Canada. Canadian Permanent Resident, arrived in Canada on 2024-06-21, authorized to work for any employer in Canada, no sponsorship required for Canadian roles.',
        'target_roles': 'Talent Acquisition Specialist, Recruiter, HR Generalist, Mid-level HR Business Partner, HR Coordinator, People Operations roles',
        'job_title': 'HR/Admin/Recruitment Professional',
        'job_search_query': 'HR recruitment talent acquisition jobs Canada US remote Canada-based applicants Nova Scotia recruiter HR Generalist HR Coordinator People Operations'
    }
    
    try:
        # Run the crew
        result = kickoff_with_rate_limit_retry(inputs)
        
        # Create HTML report
        html_report = create_crew_output_report(str(result))
        
        # Send email report
        subject = f"Daily Job Search Report - {datetime.now().strftime('%Y-%m-%d')}"
        send_email_report(subject, html_report)
        
        print(f"✅ Job Search Completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80 + "\n")
        
        # Save log
        log_file(f"✅ Job search completed successfully at {datetime.now()}")
        
    except Exception as e:
        error_msg = f"❌ Job search failed: {str(e)}"
        print(error_msg)
        print("="*80 + "\n")
        log_file(error_msg)
        
        # Send error notification email
        html = f"""
        <html><body>
            <h2>❌ Job Search Error Report</h2>
            <p><strong>Time:</strong> {datetime.now()}</p>
            <p><strong>Error:</strong> {str(e)}</p>
            <p>Please check your configuration and restart the scheduler.</p>
        </body></html>
        """
        send_email_report("⚠️ Job Search Error", html)


def log_file(message: str):
    """Log message to file."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    log_file_path = log_dir / "scheduler.log"
    with open(log_file_path, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")


def schedule_daily_job():
    """Schedule job search to run daily at specified time."""
    
    schedule_time = os.getenv("SCHEDULE_TIME", "09:00")
    
    print(f"⏰ Scheduler started - will run job search daily at {schedule_time}")
    print(f"📧 Email reports will be sent to: {os.getenv('EMAIL_RECIPIENT', 'N/A')}")
    print("Press Ctrl+C to stop the scheduler\n")
    
    log_file("Scheduler started")
    
    # Schedule the job
    schedule.every().day.at(schedule_time).do(run_job_search)
    
    # Keep scheduler running
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n🛑 Scheduler stopped by user")
            log_file("Scheduler stopped by user")
            break
        except Exception as e:
            error_msg = f"Scheduler error: {str(e)}"
            print(f"❌ {error_msg}")
            log_file(error_msg)
            time.sleep(60)  # Wait before retrying


def run_once():
    """Run job search once immediately."""
    print("Running job search once...")
    run_job_search()


if __name__ == "__main__":
    schedule_daily_job()
