from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

# Create a simple agent whose only job is to search
search_agent = Agent(
    name="SearchAgent",
    model="gemini-2.5-flash",
    tools=[google_search],
)    

# Wrap the search_agent in an AgentTool.
search_tool = AgentTool(agent=search_agent)

history_teacher = Agent(
    model='gemini-2.5-flash',
    name='HistoryTeacher',
    tools=[search_tool],
    disallow_transfer_to_parent=False,
    disallow_transfer_to_peers=False,
    description='History Teacher. Handles questions about historical events, dates, and civilizations.',
    instruction="""You are the History Teacher. You are an expert in world history, historical events, and dates.
    Help the student learn about history using search engine tool. You have access to a Google Search tool. Use it to look up specific historical facts, dates, or context if you are unsure.""",
)
