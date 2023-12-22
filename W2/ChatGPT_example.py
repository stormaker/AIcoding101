import os
import openai

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api = os.getenv("OPENAI_API_KEY")

# This code is for v1 of the openai package: pypi.org/project/openai

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You will be provided with a sentence in English, and your task is to translate it into French."
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

message_content = response.choices[0].message.content
print(message_content)

# print(response.choices[0].message)
# print(type(response.choices[0].message))
# print(response)