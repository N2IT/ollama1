import os
import requests
import json
from typing import List
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from openai import OpenAI

# constants
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj-') and len(api_key)>10:
    print('Api key looks good')
else:
    print("There might be a problem with your api key")

MODEL_GPT = 'gpt-4o-mini'
openai = 'gpt-4o-mini'
client = OpenAI(api_key=api_key)

MODEL_LLAMA = 'llama3.2'

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author") is not None}
"""

system_prompt = "You are a tutor that explains code to students"
user_prompt = "Please provide a detailed explanation of the following question: " + question

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

stream = client.chat.completions.create(
    model=MODEL_GPT,
    messages=messages,
    temperature=0.0,
    stream=True
)

response = ""
for chunk in stream:
    chunk_content = chunk.choices[0].delta.content or ''
    response += chunk_content
    print(chunk_content, end='', flush=True)  # Print chunks as they arrive

# Print final response if needed
print("\n--- Complete Response ---")
print(response)


