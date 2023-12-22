import os
import openai

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
	model="gpt-3.5-turbo",
	messages=[
		{
			"role": "assistant",
			"content": "You are an language translator that translate English into Chinese."
		},
		{
			"role": "user",
			"content": "How are you today."
		}
	],
	temperature=0.5,
	max_tokens=100,
	top_p=1,
	frequency_penalty=0.0,
	presence_penalty=0.0,
)

print(response.choices[0].message.content)
