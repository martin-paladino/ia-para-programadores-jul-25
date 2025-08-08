from langchain.chat_models import init_chat_model
import os

os.environ["GOOGLE_API_KEY"] = "tu-api-key"
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")


def get_response(user_message: str) -> str:
    """Devuelve la respuesta del modelo dado un mensaje del usuario."""

    print(f"Consultando Gemini con mensaje: {user_message}")

    try:
        messages = [
            {
                "role": "system",
                "content": """
                Eres un asistente de ventas que ayuda a los usuarios a vender sus productos.
                Tenes que tener un tono amigable y usar emojis en tus respuestas.
                """
            }
        ]

        messages.append({
            "role": "user",
            "content": user_message
        })

        response = model.invoke(messages)

        return response.content
    except Exception as e:
        return f"[Error al consultar Gemini: {e}]"
