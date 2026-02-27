from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool
import os

def create_agents():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    news_researcher = Agent(
        role="Senior Real-Time Research Analyst",
        goal="Research the given topic using real-time internet data.",
        backstory="Expert analyst who always uses tools and never hallucinates.",
        tools=[tool],
        verbose=True,
        llm=llm
    )

    news_writer = Agent(
        role="Professional News Writer",
        goal="Write structured and factual articles based only on provided research.",
        backstory="Professional journalist who never invents information.",
        verbose=True,
        llm=llm
    )

    return news_researcher, news_writer
