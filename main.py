import os
from fastapi import FastAPI, File, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai

from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_api(req:Request):
    body = await req.json()
    user_input = body.get("message", "")
    if not user_input:
        return{"reply" : "❌Please type Something."}
    
    try:
        print("User Input:", user_input)
        model = genai.GenerativeModel("gemini-2.5-flash")
        chat = model.start_chat(history=[])
        response = chat.send_message(user_input)
        print("Gemini Reply:", response.text)
        return{"reply":response.text}
    
    except Exception as e:
        print("Error:", str(e))
        return{"reply": f"❌Error:{str(e)}"}
    
    
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

for m in genai.list_models():
    if m.supported_generation_methods:
        print(m.name)