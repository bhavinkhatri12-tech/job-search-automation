#!/usr/bin/env python
import sys
from canadian_hr_job_search_assistant.crew import CanadianHrJobSearchAssistantCrew
from canadian_hr_job_search_assistant.scheduler import schedule_daily_job, run_once

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'job_search_domain': 'Canadian HR',
        'candidate_profile': 'Bhavin Khatri, HR/Admin/Recruitment Professional with 12+ years experience based in Nova Scotia, Canada',
        'target_roles': 'Talent Acquisition Specialist, HR Generalist, Mid-level HR Business Partner',
        'job_title': 'HR/Admin/Recruitment Professional',
        'job_search_query': 'HR jobs in Nova Scotia Canada Talent Acquisition Recruiter HR Generalist'
    }
    CanadianHrJobSearchAssistantCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'job_search_domain': 'Canadian HR',
        'candidate_profile': 'Bhavin Khatri, HR/Admin/Recruitment Professional with 12+ years experience based in Nova Scotia, Canada',
        'target_roles': 'Talent Acquisition Specialist, HR Generalist, Mid-level HR Business Partner',
        'job_title': 'HR/Admin/Recruitment Professional',
        'job_search_query': 'HR jobs in Nova Scotia Canada Talent Acquisition Recruiter HR Generalist'
    }
    try:
        CanadianHrJobSearchAssistantCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CanadianHrJobSearchAssistantCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'job_search_domain': 'Canadian HR',
        'candidate_profile': 'Bhavin Khatri, HR/Admin/Recruitment Professional with 12+ years experience based in Nova Scotia, Canada',
        'target_roles': 'Talent Acquisition Specialist, HR Generalist, Mid-level HR Business Partner',
        'job_title': 'HR/Admin/Recruitment Professional',
        'job_search_query': 'HR jobs in Nova Scotia Canada Talent Acquisition Recruiter HR Generalist'
    }
    try:
        CanadianHrJobSearchAssistantCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    elif command == "scheduler":
        print("Starting daily job search scheduler...")
        schedule_daily_job()
    elif command == "run-once":
        print("Running job search once...")
        run_once()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
