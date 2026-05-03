from __future__ import annotations
import datetime
from google.adk.agents import Agent
from google.adk.tools import FunctionTool, google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters 

def now() -> dict:
    """Returns the current date and time."""
    return {
        "status": "success",
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Create a simple agent whose only job is to search
search_agent = Agent(
    name="SearchAgent",
    model="gemini-2.5-flash",
    tools=[google_search],
)    

# Wrap the search_agent in an AgentTool.
search_tool = AgentTool(agent=search_agent)

# Create the time tool from our simple Python function.
time_tool = FunctionTool(func=now)

# Configure the Airbnb MCP Toolset
airbnb_mcp = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=["-y", "@openbnb/mcp-server-airbnb"],
        ),
    )
)

# The agent can now use AgentTools, MCP Toolset and FunctionTool.
travel_agent = Agent(
    name='travel_agent',
    model='gemini-2.5-flash',
    tools=[search_tool, time_tool, airbnb_mcp],
    instruction="""
You are a helpful travel agent.

Using Airbnb, help users with:
- Trip planning
- Flight suggestions
- Hotel recommendations
- Daily itineraries

You have two tools:
1. A search engine to find real-time information.
2. A tool to get the current time.

- Have access to the currenttime, use the `time_tool`.
- For any other questions requiring up-to-date information, use the search tool.

Always respond in a clear travel guide format.
""",
)
