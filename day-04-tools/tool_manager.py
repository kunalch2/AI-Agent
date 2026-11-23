from tools import get_current_time, roll_dice, generate_password

def execute_tool(user_input):
    text=user_input.lower()
    if "time" in text or "clock" in text:
        print("\n AI :", get_current_time())
    elif "dice" in user_input.lower():
        print("\nAI You rolled : ", roll_dice())

    return None
    