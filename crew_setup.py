from crewai import Crew
from tasks import create_tasks
from agents import create_agents

def create_crew():
    news_researcher, news_writer = create_agents()
    tasks = create_tasks(news_researcher, news_writer)

    crew = Crew(
        agents=[news_researcher, news_writer],
        tasks=tasks,
        verbose=True
    )

    return crew
