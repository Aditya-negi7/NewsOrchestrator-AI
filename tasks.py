from crewai import Task

def create_tasks(researcher, writer):

    research_task = Task(
    description=(
        "Use the search tool to find the latest real-time updates about {topic}. "
        "You MUST call the search tool before writing anything. "
        "Only include news from the last 48 hours. "
        "Provide source names and publication dates."
    ),
    expected_output=(
        "5 real verified news updates with:\n"
        "- Headline\n"
        "- Source\n"
        "- Date\n"
        "- Summary\n"
        "If no real-time data is found, clearly say so."
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

