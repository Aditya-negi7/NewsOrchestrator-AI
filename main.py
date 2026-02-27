from dotenv import load_dotenv
import os

load_dotenv()   # this loads .env manually

print("Gemini Key:", os.getenv("GOOGLE_API_KEY"))
print("Serper Key:", os.getenv("SERPER_API_KEY"))

from crew_setup import create_crew

def run_crew(topic):
    crew = create_crew()
    result = crew.kickoff(inputs={"topic": topic})
    return result
