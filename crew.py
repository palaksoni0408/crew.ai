from crewai import Crew, Process
from tools import yt_tool
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# Form the tech-focused crew with configurations
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.SEQUENTIAL,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
)

# Start the task execution process with inputs
result = crew.kickoff(inputs={"topic": "AI vs ML vs DL vs Data Science"})
print(result)