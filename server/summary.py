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
    {"role": "user", "content": "What is 2 + 2? Wrong answers only."},
]

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    """
    A utility class to represent a Website that we have scraped, now with links
    """

    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""
        links = [link.get('href') for link in soup.find_all('a')]
        self.links = [link for link in links if link]

    def get_contents(self):
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"

payload = {
    "model": MODEL,
    "messages": messages,
    "stream": False,
}

print("Sending request...")
ed = Website("https://herapathways.com")
print(ed.get_contents())
print(ed.links)


