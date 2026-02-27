from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os

def create_agents():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=1,
        google_api_key=os.getenv("")
    )

    news_researcher = Agent(
        role="News Researcher",
        goal="Research latest news",
        backstory="Expert news analyst",
        verbose=True,
        llm=llm
    )

    news_writer = Agent(
        role="News Writer",
        goal="Write structured article",
        backstory="Professional journalist",
        verbose=True,
        llm=llm
    )

    return news_researcher, news_writer