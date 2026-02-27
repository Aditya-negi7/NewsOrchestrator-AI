from crewai import Task
from agents import smart_researcher, smart_writer

research_task = Task(
    description=(
        "Search the internet for the latest developments, trends, or news "
        "about the topic: {topic}. "
        "Focus only on recent information from the last 48 hours. "
        "Provide source name and publication date."
    ),
    expected_output=(
        "A structured research report including:\n"
        "- 5 Latest Updates\n"
        "- Headline\n"
        "- Source Name\n"
        "- Publication Date\n"
        "- 2-3 line summary for each"
    ),
    agent=smart_researcher
)

write_task = Task(
    description=(
        "Using the research provided, write a professional news-style article "
        "with clear headings and structured paragraphs."
    ),
    expected_output=(
        "A well-structured article with:\n"
        "- Engaging headline\n"
        "- Introduction\n"
        "- Key developments\n"
        "- Conclusion\n"
        "No fake information."
    ),
    agent=smart_writer
)
