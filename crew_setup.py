from crewai import Crew
from agents import create_agents
from tasks import create_tasks

def create_crew():

    researcher, writer = create_agents()
    research_task, write_task = create_tasks(researcher, writer)

    crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=True
)

    return crew

