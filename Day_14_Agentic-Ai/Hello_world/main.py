from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() #load variables from .env

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5-mini",
    messages =[

        {"role": "user", "content": "Hey, I am Gabriel Okom. Nice to meet you!"}
    ]
)

print(response.choices[0].message.content)