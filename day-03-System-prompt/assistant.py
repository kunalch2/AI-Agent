from openai import OpenAI
from dotenv import load_dotenv
import os

#load config
load_dotenv()

#Create AI client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("="*40)
print("MY AI ASSISTANT")
print("="*40)


roles = {
    "1":"You are a friendly AI teacher. Explain every concept in simple language with real-life examples.",
    "2":"You are a senior python developer. Explain programming concepts clearly and always include python examples"

}

print("\nChoose your assistant\n")
print("1. Teacher")
print("2. Python Expert")

choice = input("\n Enter your choice: ")

messages = [
    {
        "role":"system",
        "content":roles.get(choice,"You are a helpful Ai assistant")
    }

]

while True:

    user_input = input("\nYou:")

    messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )

    if user_input.lower() == "quit":
        print("\nAI : GoodBye! Have a great day")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages        
    )

    ai_reply=response.choices[0].message.content

    messages.append(
        {
            "role":"assistant",
            "content":ai_reply
        }
    )


    print("\nAI:", ai_reply)