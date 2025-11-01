from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import os

# Load .env early so environment variables are available when creating the LLM
load_dotenv()

# If an OPENAI_API_KEY is provided in the environment, keep it available for libraries
if os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Instantiate the LLM after environment is loaded
llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL_NAME", "gpt-4o"))

blog_researcher = Agent(
    role='Blog Researcher from YouTube Videos',
    goal='Get the relevant video content for the topic {topic} from the specified YouTube channel',
    verbose=True,
    memory=True,
    backstory='Expert in understanding videos in AI, Data Science, Machine Learning and GenAI and providing concise summaries.',
    tools=[yt_tool],
    llm=llm,                # 👈 REQUIRED
    allow_delegation=True,
)

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate a compelling technical blog based on the video content for {topic} from the YouTube channel',
    verbose=True,
    memory=True,
    backstory='With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate.',
    tools=[yt_tool],
    llm=llm,                # 👈 REQUIRED
    allow_delegation=False,
)
