from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool
import os

def create_agents():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    news_researcher = Agent(
    role="Senior Real-Time Research Analyst",
    goal=(
        "You MUST use the search tool to gather real-time information. "
        "You are strictly forbidden from answering without using the tool."
    ),
    backstory=(
        "You are an investigative journalist who ALWAYS searches the internet."
        "before providing any answer. If you do not use the tool, your answer is invalid."
    ),
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
