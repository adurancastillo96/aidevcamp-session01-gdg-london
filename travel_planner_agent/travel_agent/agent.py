from __future__ import annotations
import datetime
from zoneinfo import ZoneInfo
from urllib.parse import quote_plus

from google.adk.agents import Agent
from google.adk.tools import FunctionTool, google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters 

def search_flights_simple(origin: str, destination: str, date: str) -> dict:
    """Returns a Google Flights search link."""
    query = f"Flights from {origin} to {destination} on {date}"
    url = f"https://www.google.com/travel/flights?q={quote_plus(query)}"
    return {
        "status": "success",
        "message": "Here are available flight options.",
        "origin": origin,
        "destination": destination,
        "date": date,
        "booking_url": url,
    }

def now() -> dict:
    """Returns the current date and time in Europe/Madrid."""
    return {
        "status": "success",
        "current_time": datetime.datetime.now(ZoneInfo("Europe/Madrid")).strftime("%Y-%m-%d %H:%M:%S")
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
            args=[
                "-y",
                "@openbnb/mcp-server-airbnb@0.1.2",
                "--ignore-robots-txt",
            ],
        ),
        timeout=30,
    )
)

# Create the flight_agent
flight_agent = Agent(
    name="flight_agent",
    model="gemini-2.5-flash",
    description="Handles flight searches and returns Google Flights links.",
    tools=[search_flights_simple],
    instruction="""
You are a helpful flight booking assistant.

Your job is to help users find flights.

Rules:
- Use search_flights_simple when the user asks for flights.
- If origin, destination, or travel date is missing, ask one short follow-up question.
- Always include the booking link in your response.
- Keep the answer short and practical.
""",
)

# Wrap the flight_agent in an AgentTool.
flight_tool = AgentTool(agent=flight_agent)

# Create the itinerary agent
itinerary_agent = Agent(
    name="itinerary_agent",
    model="gemini-2.5-flash",
    description="Creates day-by-day travel itineraries based on destination, trip length, and interests.",
    tools=[time_tool],
    instruction="""
You are a helpful itinerary planner.

Your job is to create practical travel itineraries.

Rules:
- Build a clear day-by-day itinerary.
- Use morning / afternoon / evening structure when useful.
- Group nearby places together to keep the plan realistic.
- Suggest food, sightseeing, and local experiences when relevant.
- If destination, trip length, or interests are missing, ask one short follow-up question.
- Use the now tool only if the user asks for the current date or time.
- Keep the itinerary easy to read.
""",
)

# Wrap the itinerary_agent in an AgentTool.
itinerary_tool = AgentTool(agent=itinerary_agent)

# The agent can now use AgentTools, MCP Toolset and FunctionTool.
travel_agent = Agent(
    name='travel_agent',
    model='gemini-2.5-flash',
    tools=[search_tool, time_tool, airbnb_mcp, flight_tool, itinerary_tool],
    instruction="""
You are a helpful travel agent.

Your job is to help the user plan trips, find flights, Airbnb stays, and create itineraries.

You have five tools:
1. search_tool: a search engine to find real-time information.
2. time_tool: a tool to get the current time.
3. airbnb_mcp: Airbnb tool to search for flights, hotels, and other travel-related services.
4. flight_tool: Flight tool to search for flights.
5. itinerary_tool: Itinerary tool to create day-by-day travel itineraries.

Rules:
- Delegate to the correct specialist based on the user's request.
- If the user asks for a complete trip, help with flights, stay, and itinerary.
- If the user has not provided enough details, ask one short follow-up question.
- Keep answers simple and helpful.
- When finished, reply with "DONE".
""",
)
