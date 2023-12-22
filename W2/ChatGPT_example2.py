import os
import openai

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api = os.getenv("OPENAI_API_KEY")

# This code is for v1 of the openai package: pypi.org/project/openai

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for part in stream:
    print(part.choices[0].delta.content or "")

