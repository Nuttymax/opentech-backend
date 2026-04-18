import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="OpenTech AI Solutions API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://nuttymax-opentech.b12sites.com",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str
    conversation_id: str = None

class ChatResponse(BaseModel):
    response: str
    conversation_id: str

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "OpenTech AI Solutions API",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful business assistant for OpenTech AI Solutions. Help customers with inquiries about our AI chatbot services."
                },
                {
                    "role": "user",
                    "content": request.message
                }
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        bot_response = response.choices[0].message.content
        
        return ChatResponse(
            response=bot_response,
            conversation_id=request.conversation_id or "new"
        )
    
    except Exception as e:
        return ChatResponse(
            response=f"I apologize, but I'm experiencing technical difficulties. Please try again later.",
            conversation_id=request.conversation_id or "error"
        )

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
