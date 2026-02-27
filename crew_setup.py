from crewai import Crew
from agents import create_agents
from tasks import create_tasks

def create_crew():
    news_researcher, news_writer = create_agents()
    tasks = create_tasks(news_researcher, news_writer)

    crew = Crew(
        agents=[news_researcher, news_writer],
        tasks=tasks,
        verbose=True
    )

    return crew
