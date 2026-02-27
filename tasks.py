from crewai import Task

def create_tasks(news_researcher, news_writer):

    # Research Task
    research = Task(
    description=(
        "If recency_mode is TRUE, you MUST search for articles "
        "published between {three_days_ago} and {today}. "
        "Start with today's or yesterday's news first. "
        "Do NOT include articles older than 4 days.\n\n"

        "If recency_mode is FALSE, you may include authoritative "
        "articles regardless of publication date, prioritizing "
        "high-quality sources and relevance over recency.\n\n"

        "Always clearly mention publication date, time, source name, "
        "and URL. Cover diverse aspects of the topic."
    ),
    expected_output=(
        "Return a structured list of at least 5 articles including:\n"
        "- Headline\n"
        "- Source\n"
        "- Publication Date\n"
        "- Publication Time\n"
        "- URL\n"
        "- 2–4 key bullet insights"
    ),
    agent=news_researcher,
)
    return [research, write]
