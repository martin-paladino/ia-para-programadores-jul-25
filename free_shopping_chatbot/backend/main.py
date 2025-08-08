from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from chatbot_service import get_response


app = FastAPI()

# Permitir CORS para frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    messages = data.get("messages", [])

    print(f"Mensaje del usuario: {messages}")

    reply = get_response(messages)
    return JSONResponse({"reply": reply})

