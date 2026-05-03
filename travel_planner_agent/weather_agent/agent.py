from google.adk.agents.llm_agent import Agent
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

weather_agent = Agent(
    model="gemini-2.5-flash",
    name="weather_agent",
    tools=[search_tool],
    instruction="""
You are a weather assistant.

Using search engine tool, help users with:
- Current weather
- Forecasts
- Best time to travel based on weather
- Packing suggestions

Keep answers short and practical.
"""
)
