from google import genai
from google.genai import types
import os

class ChatbotService:
    def __init__(self):
        # Usa la API key desde variable de entorno o ponla aquí (no recomendado en producción)
        api_key = "AIzaSyABNfs6v9Q08LJoKMJZluGPhu-0XR_6VtM"
        self.client = genai.Client(api_key=api_key)

    def get_response(self, user_message: str) -> str:
        # Prompt simple, se puede mejorar con contexto o instrucciones
        print(f"Consultando Gemini con mensaje: {user_message}")
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_message,
                config=types.GenerateContentConfig(
                    system_instruction="Sos un asistente de Free Shopping. Ayuda a los usuarios a vender productos y resolver dudas o reclamos.",
                    #max_output_tokens=500,
                    temperature=0.2
                ),
            )
            print(response)
            if not hasattr(response, 'text') or response.text is None or not str(response.text).strip():
                return "Lo siento, no pude generar una respuesta en este momento. ¿Podés intentar de nuevo o reformular tu consulta?"
            return response.text
        except Exception as e:
            return f"[Error al consultar Gemini: {e}]"
