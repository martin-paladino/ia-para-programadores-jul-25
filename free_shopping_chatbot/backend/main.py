
# Importaciones principales de FastAPI y utilidades
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Importa la función que genera la respuesta del chatbot
from chatbot_service import get_response

# Inicializa la aplicación FastAPI
app = FastAPI()

# Configura el middleware CORS para permitir peticiones desde
# cualquier origen (ideal para desarrollo local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los headers
)

# Endpoint principal para el chat
@app.post("/chat")
async def chat(request: Request):
    # Obtiene el cuerpo de la petición como JSON
    data = await request.json()
    # Extrae la lista de mensajes enviados por el frontend
    messages = data.get("messages", [])
    # Genera la respuesta usando el modelo Gemini
    reply = get_response(messages)
    # Devuelve la respuesta en formato JSON
    return JSONResponse({"reply": reply})
