#!/usr/bin/env python
"""Email utility module for sending job search reports."""

import smtplib
import os
import html
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


def send_email_report(subject: str, body: str, attachments: list = None):
    """
    Send email report of job search results.
    
    Args:
        subject: Email subject line
        body: Email body content (HTML)
        attachments: List of file paths to attach
    """
    try:
        sender_email = os.getenv("EMAIL_SENDER") or os.getenv("EMAIL_USER", "bhavinkhatri12@gmail.com")
        sender_password = os.getenv("EMAIL_PASSWORD", "")
        recipient_email = os.getenv("EMAIL_RECIPIENT", "bhavinkhatri12@gmail.com")
        smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.getenv("SMTP_PORT", 587))
        
        if not sender_password:
            print("⚠️  EMAIL_PASSWORD not configured. Email report skipped.")
            return False
        
        # Create message
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = recipient_email
        
        # Add HTML body
        part = MIMEText(body, "html")
        message.attach(part)
        
        # Add attachments if provided
        if attachments:
            from email.mime.base import MIMEBase
            from email import encoders
            
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename= {os.path.basename(file_path)}'
                        )
                        message.attach(part)
        
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        
        print(f"✅ Email report sent to {recipient_email}")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("❌ Email Authentication Failed. Check EMAIL_PASSWORD (use Gmail App Password).")
        return False
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        return False


def create_html_report(job_results: dict) -> str:
    """Create HTML formatted email report of job search results."""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f5f5f5; }}
            .container {{ max-width: 800px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 8px; }}
            .header {{ background-color: #2c3e50; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
            .section {{ margin-bottom: 20px; }}
            .section-title {{ background-color: #3498db; color: white; padding: 10px 15px; border-radius: 4px; margin-bottom: 10px; font-weight: bold; }}
            .job-item {{ border-left: 4px solid #2ecc71; padding: 15px; margin-bottom: 10px; background-color: #f9f9f9; border-radius: 4px; }}
            .job-title {{ font-weight: bold; font-size: 16px; color: #2c3e50; }}
            .job-company {{ color: #27ae60; font-weight: bold; margin: 5px 0; }}
            .job-details {{ color: #666; margin-top: 10px; line-height: 1.6; }}
            .footer {{ text-align: center; color: #999; font-size: 12px; padding-top: 20px; border-top: 1px solid #ddd; margin-top: 20px; }}
            .stats {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 20px; }}
            .stat-box {{ background-color: #ecf0f1; padding: 15px; border-radius: 4px; text-align: center; }}
            .stat-number {{ font-size: 28px; font-weight: bold; color: #2ecc71; }}
            .stat-label {{ color: #666; margin-top: 5px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🔍 Daily Job Search Report</h1>
                <p>Generated on {timestamp}</p>
                <p>Candidate: Bhavin Khatri - HR/Admin/Recruitment Professional</p>
            </div>
            
            <div class="section">
                <div class="stats">
                    <div class="stat-box">
                        <div class="stat-number">{job_results.get('total_jobs', 0)}</div>
                        <div class="stat-label">Jobs Found</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">{job_results.get('applied_count', 0)}</div>
                        <div class="stat-label">Applications Sent</div>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <div class="section-title">📋 Job Opportunities Found</div>
                {format_jobs_html(job_results.get('jobs', []))}
            </div>
            
            <div class="section">
                <div class="section-title">✅ Applications Status</div>
                <div class="job-details">
                    <p><strong>Status:</strong> {job_results.get('status', 'Processing...')}</p>
                    <p><strong>Applied Count:</strong> {job_results.get('applied_count', 0)} jobs</p>
                    <p><strong>Next Run:</strong> Tomorrow at 09:00 AM (Canada/Atlantic Time)</p>
                </div>
            </div>
            
            <div class="footer">
                <p>This is an automated report from Canadian HR Job Search Assistant</p>
                <p>To adjust schedule or settings, edit the .env file and restart the scheduler</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html


def create_crew_output_report(report_text: str) -> str:
    """Create an HTML email from the CrewAI final report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    safe_report = html.escape(report_text).replace("\n", "<br>")

    return f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f5f5f5; color: #222; }}
            .container {{ max-width: 900px; margin: 0 auto; background-color: white; padding: 24px; border-radius: 8px; }}
            .header {{ background-color: #2c3e50; color: white; padding: 18px 20px; border-radius: 8px; margin-bottom: 20px; }}
            .report {{ line-height: 1.6; font-size: 14px; }}
            .footer {{ color: #777; font-size: 12px; padding-top: 18px; border-top: 1px solid #ddd; margin-top: 24px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Daily Job Search Report</h1>
                <p>Generated on {timestamp}</p>
                <p>Candidate: Bhavin Khatri - HR/Admin/Recruitment Professional</p>
            </div>
            <div class="report">{safe_report}</div>
            <div class="footer">
                <p>This is an automated report from Canadian HR Job Search Assistant.</p>
            </div>
        </div>
    </body>
    </html>
    """


def format_jobs_html(jobs: list) -> str:
    """Format job list as HTML."""
    if not jobs:
        return "<p>No jobs found in this search.</p>"
    
    html = ""
    for job in jobs[:10]:  # Show top 10 jobs
        html += f"""
        <div class="job-item">
            <div class="job-title">{job.get('title', 'N/A')}</div>
            <div class="job-company">{job.get('company', 'N/A')}</div>
            <div class="job-details">
                <p><strong>Location:</strong> {job.get('location', 'N/A')}</p>
                <p><strong>Salary:</strong> {job.get('salary', 'Not specified')}</p>
                <p><strong>Link:</strong> <a href="{job.get('link', '#')}">{job.get('link', 'View Job')}</a></p>
            </div>
        </div>
        """
    
    return html
