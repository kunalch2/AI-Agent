from tools import get_current_time, roll_dice, generate_password
from planner import choose_tool

def execute_tool(user_input):
    text=user_input.lower()
    tool = choose_tool(user_input)
    print(tool)

    if tool == "get_current_time":
        result = get_current_time()
    elif tool == "roll_dice":
        result = roll_dice()
    elif tool == "generate_password":
        result = generate_password()
    else:
        result = None        
    return result
    