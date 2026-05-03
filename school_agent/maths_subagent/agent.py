from google.adk.agents import Agent

# Tools
def calculate(expression: str) -> float:
    """
    Evaluates a mathematical expression and returns the result.
    
    Args:
        expression: The math expression to evaluate (e.g. '2 + 2 * 3')
        
    Returns:
        float: The result of the calculation.
    """
    import math
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    
    try:
        # A relatively safe eval restricting to math module functions
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return float(result)
    except Exception as e:
        print(f"Error evaluating '{expression}': {e}")
        return 0.0


maths_teacher = Agent(
    model='gemini-2.5-flash',
    name='MathsTeacher',
    tools=[calculate],
    disallow_transfer_to_parent=False,
    disallow_transfer_to_peers=False,
    description='Maths Teacher. Handles questions about mathematics, equations, and calculations.',
    instruction="""You are the Maths Teacher. You are an expert in mathematics, algebra, calculus, and geometry.
    Help the student solve math problems. You have access to a calculator tool. Use it to evaluate expressions if needed.
    Explain the steps logically to the student.""",
)
