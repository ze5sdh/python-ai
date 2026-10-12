import requests
from openai import OpenAI
from api_key import KEY

client = OpenAI(api_key=KEY, base_url="https://open.bigmodel.cn/api/paas/v4/")

messages = []  

def chat_bot(history):
    response = client.chat.completions.create(
        model="glm-5.3-flash",
        messages=history,  
        temperature=0.7,
    )
    return response.choices[0].message.content

while True:
    kiki = input("jdid: ")
    if kiki.lower() == "exit":
        break

    messages.append({"role": "user", "content": kiki}) 
    reply = chat_bot(messages)
    messages.append({"role": "assistant", "content": reply})  

    print(reply)