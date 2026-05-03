from google.adk.agents import Agent

from .english_subagent.agent import english_teacher
from .maths_subagent.agent import maths_teacher
from .science_subagent.agent import science_teacher
from .history_subagent.agent import history_teacher
from .geography_subagent.agent import geography_teacher
from .computer_science_subagent.agent import computer_science_teacher

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    sub_agents=[
        english_teacher,
        maths_teacher,
        science_teacher,
        history_teacher,
        geography_teacher,
        computer_science_teacher
    ],
    description="School Coordinator. Routes queries to the appropriate subject teacher.",
    instruction="""You are the School Coordinator. Your job is to analyze the student's request and transfer them to the most appropriate Subject Teacher.
    - Transfer to EnglishTeacher for reading, writing, grammar, and literature.
    - Transfer to MathsTeacher for calculations, equations, and math concepts.
    - Transfer to ScienceTeacher for biology, chemistry, and physics.
    - Transfer to HistoryTeacher for historical facts and events.
    - Transfer to GeographyTeacher for countries, capitals, and natural landmarks.
    - Transfer to ComputerScienceTeacher for programming and software.
    
    If the student asks a general question, you can answer it yourself. Always be polite and helpful.""",
)
