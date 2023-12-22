import os
import openai

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api = os.getenv("OPENAI_API_KEY")

# Ensure the API key is passed correctly to the client
client = OpenAI(api_key=openai_api)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "assistant",
            "content": "You will be provided with a sentence in English, and your task is to translate it into Chinese."
        },
        {
            "role": "user",
            "content": "My name is Jane. What is yours?"
        }
    ],
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Access the 'content' field of the response directly
print(response.choices[0].message.content)
