
# Importa la función para inicializar el modelo de chat de LangChain
from langchain.chat_models import init_chat_model
# Importa el módulo para manejar variables de entorno
import os

# Configura la clave de API de Google para acceder al modelo Gemini
os.environ["GOOGLE_API_KEY"] = "tu_api_key_aqui"

# Inicializa el modelo de chat especificando el modelo y el proveedor
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")



def get_response(messages: list[dict]) -> list[dict]:
    """
    Genera una respuesta del asistente de ventas usando el modelo Gemini.

    Args:
        messages (list[dict]): Lista de mensajes en formato dict, cada uno con 'role' y 'content'.

    Returns:
        list[dict]: Lista de mensajes incluyendo la respuesta del asistente.
    """
    try:
        # Mensaje de sistema para definir el comportamiento del asistente
        system_message = {
            "role": "system",
            "content": (
                """
                Eres un asistente de ventas que ayuda a los usuarios a vender sus productos.\n"
                "Tenes que tener un tono amigable y usar emojis en tus respuestas."
                """
            )
        }

        # Inserta el mensaje de sistema al inicio de la conversación
        messages.insert(0, system_message)

        # Invoca el modelo para obtener la respuesta del asistente
        response = model.invoke(messages)

        # Agrega la respuesta del asistente a la lista de mensajes
        messages.append({
            "role": "assistant",
            "content": response.content
        })

        # Elimina el mensaje de sistema para no devolverlo al frontend
        messages.pop(0)

        # Devuelve la conversación actualizada
        return messages
    except Exception as e:
        # Devuelve un mensaje de error si ocurre una excepción
        return f"[Error al consultar Gemini: {e}]"
