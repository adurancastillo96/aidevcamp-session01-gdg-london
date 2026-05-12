# AI DevCamp Session 01 - GDG London

Welcome to the repository for the first session of the AI DevCamp hosted by GDG London!

This repository contains two main Google Agent Development Kit (ADK) projects:

## 1. Travel Planner Agent (`travel_planner_agent`)
This agent was developed as an **in-class example**. It demonstrates the basic capabilities of the ADK by building a multi-agent system that helps plan a trip.

## 2. School Agent (`school_agent`)
This agent is an **assignment**. It is a more complex multi-agent system functioning as a school coordinator that routes queries to specialized subject teacher sub-agents (Maths, Science, English, History, Geography, and Computer Science).

## How to Run

These projects use `uv` for dependency management and execution. Always make sure to prefix the commands with `uv run` when interacting with the ADK.

To start, navigate into one of the agent directories (e.g., `cd travel_planner_agent`).

### Terminal Chat
To start an interactive chat with the agent in your terminal, run:
```bash
uv run adk chat
```

### ADK Web Development Interface
To start the ADK web development UI, run:
```bash
uv run adk dev
```
