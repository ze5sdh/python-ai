import requests 
from openai import OpenAI
import re

def get_page(url):
    response = requests.get(url)
    response.encoding = "utf-8"

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to receive any page from: {url}")
        return None

def clean_html(html):
   cleaner = re.sub(r"<[^>]+>", "", html)
   return cleaner

client = OpenAI(api_key="", base_url="https://open.bigmodel.cn/api/paas/v4/")

def generate_response(prompt):
   response = client.chat.completions.create(
      model="glm-5.3-flash",
      messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
   )


   return response.choices[0].message.content

print(generate_response("What is the capital of France?"[ : 3000]))