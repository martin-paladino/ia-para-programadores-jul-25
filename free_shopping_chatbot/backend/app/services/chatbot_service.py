from langchain.chat_models import init_chat_model
import os


class ChatbotService:
    def __init__(self):
        # definir la API key desde la variable de entorno GOOGLE_API_KEY
        os.environ["GOOGLE_API_KEY"] = "tu_api_key"
        self.model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

    def get_response(self, user_message: str) -> str:
        # Prompt simple, se puede mejorar con contexto o instrucciones
        print(f"Consultando Gemini con mensaje: {user_message}")
        try:
            response = self.model.invoke(user_message)
            print(response)
            # LangChain Gemini retorna el texto en response.content
            return response.content
        except Exception as e:
            return f"[Error al consultar Gemini: {e}]"
