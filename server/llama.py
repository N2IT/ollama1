# imports

import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
import ollama
import json

OLLAMA_API_URL = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = 'llama3.2'

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "what is 2 + 2? Wrong answers only."},
]

payload = {
    "model": MODEL,
    "messages": messages,
    "stream": False,
}

print("Sending request...")
response = ollama.chat(model=MODEL, messages=messages)
print(f"Response: {response['message']['content']}")

