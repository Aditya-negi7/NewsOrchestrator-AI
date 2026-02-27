from crewai import Task

def create_tasks(researcher, writer):

    research_task = Task(
        description=(
            "Search the internet for the latest developments about {topic}. "
            "Focus on information from the last 48 hours. "
            "Include source name and publication date."
        ),
        expected_output=(
            "5 latest updates with:\n"
            "- Headline\n"
            "- Source\n"
            "- Date\n"
            "- Short summary"
        ),
        agent=researcher
    )

    write_task = Task(
        description=(
            "Write a professional news article using only the research provided."
        ),
        expected_output=(
            "Structured article with headline, introduction, body, and conclusion."
        ),
        agent=writer
    )

    return research_task, write_task
