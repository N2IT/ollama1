# imports

import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
import json

OLLAMA_API_URL = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = 'llama3.2'

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"},
]

payload = {
    "model": MODEL,
    "messages": messages,
    "stream": False,
}

print("Sending request...")
response = requests.post(OLLAMA_API_URL, headers=HEADERS, json=payload)
print(f"Status code: {response.status_code}")
print(f"Response: {response.json()}")

