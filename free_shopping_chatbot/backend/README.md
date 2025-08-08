# Backend Free Shopping Chatbot

Backend mínimo con FastAPI para un chatbot que llama a Gemini (vía LangChain).

## Estructura simplificada

```
backend/
├─ main.py               # FastAPI app (ruta POST /chat)
└─ chatbot_service.py    # Lógica del chatbot (funciones)
```

## Ejecutar en desarrollo

1. (Opcional) Exporta tu API key de Google en la terminal:

   - macOS/Linux:
     ```bash
     export GOOGLE_API_KEY="TU_API_KEY"
     ```

   - Windows (PowerShell):
     ```powershell
     $env:GOOGLE_API_KEY="TU_API_KEY"
     ```

   Si no la defines, el código usará el placeholder `"tu_api_key"` (cámbialo en clase/lab).

2. Instala dependencias (en un virtualenv si prefieres):
   ```bash
   pip install -r requirements.txt
   ```

3. Arranca el servidor desde la carpeta `backend/`:
   ```bash
   uvicorn main:app --reload
   ```

4. Endpoint disponible:
   - POST `/chat` con body JSON `{ "message": "Hola" }`

