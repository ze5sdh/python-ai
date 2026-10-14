import requests
from openai import OpenAI
from api_key import KEY


client =OpenAI(api_key=KEY, base_url="https://open.bigmodel.cn/api/paas/v4/")

def Ai_bot(history):
    response = client.chat.completions.create(
        model="glm-5.3-flash",
        messages=history
         
        
    ) 
    return response.choices[0].message.content

messages = [{"role": "system", "content": "You are a pirate. Answer everything in pirate speak."}]

while True:
    user_text = input("You: ")
    if user_text.lower() == "exit":
        break
    messages.append({"role": "user", "content": user_text})
    reply = Ai_bot(messages)          
    messages.append({"role": "assistant", "content": reply})
    print("AI:", reply)