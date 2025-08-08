from langchain.chat_models import init_chat_model
import os

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "tu_api_key")
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")


def get_response(user_message: str) -> str:
    """Devuelve la respuesta del modelo dado un mensaje del usuario."""

    print(f"Consultando Gemini con mensaje: {user_message}")

    try:
        response = model.invoke(user_message)

        return response.content
    except Exception as e:
        return f"[Error al consultar Gemini: {e}]"
