from google.adk.agents.llm_agent import Agent
from .travel_agent.agent import travel_agent
from .weather_agent.agent import weather_agent
from .email_agent.agent import email_agent

# NOTE: The Gmail API must be enabled in your GCP project (gemini-agent-mirror).
# If not already enabled, visit:
# https://console.cloud.google.com/apis/library/gmail.googleapis.com

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="Main router agent that sends tasks to sub-agents.",
    sub_agents=[travel_agent, weather_agent],
    instruction="""
You are a helpful travel assistant.

Route user requests:

- If user asks about travel, trips, flights, current time → use travel_agent
- If user asks about weather, temperature, forecast → use weather_agent

If unsure, respond directly.
""",
)