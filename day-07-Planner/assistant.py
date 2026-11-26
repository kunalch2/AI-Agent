from openai import OpenAI
from dotenv import load_dotenv
from tool_manager import execute_tool
from tools import read_text_file


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

    text = user_input.lower()

    if text.startswith("ask"):
        parts = user_input.split(maxsplit=2)
        print(parts)
        filename = parts[1]
        question = parts[2]
        
        file_content = read_text_file(filename=filename)  
        print(file_content)  
        prompt = f"""You are given the document. Answer the User's question using only the information present in the document. If the answer is not available, say: I could not find that information in the document. Document: {file_content} Question: {question}"""

        response = client.chat.completions.create(
            model = os.getenv("MODEL"),
            messages=[
                {
                    "role":"system",
                    "content":"You are helpful assistant"
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        print(response.choices[0].message.content)

    print("+"*10)
    tool_result = execute_tool(user_input)

    prompt = f""" The user asked: {user_input} 
            The tool returned: {tool_result} 
            Answer the user naturally.  """


    messages.append(
        {
            "role":"user",
            "content":prompt
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