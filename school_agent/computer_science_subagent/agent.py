from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search

# Create a simple agent whose only job is to search
search_agent = Agent(
    name="SearchAgent",
    model="gemini-2.5-flash",
    tools=[google_search],
)    

# Wrap the search_agent in an AgentTool.
search_tool = AgentTool(agent=search_agent)

computer_science_teacher = Agent(
    model='gemini-2.5-flash',
    name='ComputerScienceTeacher',
    tools=[search_tool],
    disallow_transfer_to_parent=False,
    disallow_transfer_to_peers=False,
    description='Computer Science Teacher. Handles questions about programming, software, and logic.',
    instruction="""You are the Computer Science Teacher. You are an expert in programming, software engineering, and logic.
    Help the student learn about programming concepts using google search engine tool if you don't have the answer. You have access to a Google Search tool. Use it to look up specific programming syntax, recent technologies, or documentation if needed.""",
)