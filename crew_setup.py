from crewai import Crew
from agents import smart_researcher, smart_writer
from tasks import research_task, write_task

def create_crew():
    crew = Crew(
        agents=[smart_researcher, smart_writer],
        tasks=[research_task, write_task],
        verbose=2
    )
    return crew
