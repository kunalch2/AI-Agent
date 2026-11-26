from datetime import datetime
from fastmcp import FastMCP
import random

mcp = FastMCP("Time Server")

@mcp.tool()
def current_time():
    """Return the current date and time."""

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

@mcp.tool()
def  roll_dice():
    """Roll a six-sided dice."""

    return random.randint(1,6)

@mcp.tool()
def generate_password(length=12):
    """Generate a secure random password"""

    characters = (
        string.ascii_letters + string.digits + string.punctuation
    )
    password=""
    for _ in range(length):
        password += secrets.choice(characters)

    return password

if __name__=="__main__":
    print("Strting MCP Server...")
    mcp.run()