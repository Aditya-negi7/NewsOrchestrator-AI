from crewai import Crew
from tasks import create_tasks
from agents import create_agents

def create_crew(topic):

    news_researcher, news_writer = create_agents()
    research, write = create_tasks(topic)

    crew = Crew(
        agents=[news_researcher, news_writer],
        tasks=[research, write],
        verbose=True
    )

    return crew