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

geography_teacher = Agent(
    model='gemini-2.5-flash',
    name='GeographyTeacher',
    tools=[search_tool],
    disallow_transfer_to_parent=False,
    disallow_transfer_to_peers=False,
    description='Geography Teacher. Handles questions about geography, countries, capitals, and landmarks.',
    instruction="""You are the Geography Teacher using search engine tool. You are an expert in world geography, countries, capitals, and natural landmarks.
    Help the student learn about geography. You have access to a Google Search tool. Use it to look up specific geographical facts, population data, or locations if needed.""",
)
