import os
import time
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

# ---------------- LOAD ENV ----------------
load_dotenv()

# ---------------- GLOBAL LLM ----------------
llm = LLM(
    model="llama-3.3-70b-versatile",
    api_base="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------- EMAIL FUNCTION ----------------
def send_email(report):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECIPIENT")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))

    if not all([sender, password, receiver, smtp_server, smtp_port]):
        print("❌ Email configuration missing in .env")
        return

    msg = MIMEText(report)
    msg["Subject"] = "📊 Daily Job Search Report"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Email failed:", e)


# ---------------- CREW CLASS ----------------
@CrewBase
class CanadianHrJobSearchAssistantCrew:

    # -------- AGENTS --------

    @agent
    def job_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["job_research_specialist"],
            tools=[ScrapeWebsiteTool(), SerperDevTool()],
            reasoning=False,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            llm=llm
        )

    @agent
    def job_matching_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["job_matching_analyst"],
            tools=[],
            reasoning=False,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            llm=llm
        )

    @agent
    def resume_optimization_expert(self) -> Agent:
        return Agent(
            config=self.agents_config["resume_optimization_expert"],
            tools=[],
            reasoning=False,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            llm=llm
        )

    @agent
    def cover_letter_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["cover_letter_specialist"],
            tools=[],
            reasoning=False,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            llm=llm
        )

    @agent
    def application_package_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config["application_package_coordinator"],
            tools=[],
            reasoning=False,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            llm=llm
        )

    @agent
    def job_search_tracker(self) -> Agent:
        return Agent(
            config=self.agents_config["job_search_tracker"],
            tools=[],
            reasoning=False,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            llm=llm
        )

    @agent
    def daily_job_search_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config["daily_job_search_reporter"],
            tools=[],
            reasoning=False,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            llm=llm
        )

    # -------- TASKS --------

    @task
    def research_job_listings(self) -> Task:
        return Task(config=self.tasks_config["research_job_listings"])

    @task
    def score_and_match_jobs(self) -> Task:
        return Task(config=self.tasks_config["score_and_match_jobs"])

    @task
    def optimize_resume(self) -> Task:
        return Task(config=self.tasks_config["optimize_resume"])

    @task
    def create_cover_letters(self) -> Task:
        return Task(config=self.tasks_config["create_cover_letters"])

    @task
    def prepare_application_packages(self) -> Task:
        return Task(config=self.tasks_config["prepare_application_packages"])

    @task
    def track_job_applications(self) -> Task:
        return Task(config=self.tasks_config["track_job_applications"])

    @task
    def generate_daily_report(self) -> Task:
        return Task(config=self.tasks_config["generate_daily_report"])

    # -------- CREW --------

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )


# ---------------- MAIN RUNNER ----------------
if __name__ == "__main__":
    print("🚀 Starting Job Search Crew...")

    crew_instance = CanadianHrJobSearchAssistantCrew().crew()

    try:
        result = crew_instance.kickoff()
    except Exception as e:
        print("⚠️ Error occurred, retrying in 10 seconds:", e)
        time.sleep(10)
        result = crew_instance.kickoff()

    print("✅ Crew finished execution")

    # ---------------- SEND EMAIL ----------------
    send_email(str(result))