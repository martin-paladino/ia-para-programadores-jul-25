
# Importa la función para inicializar el modelo de chat de LangChain
from langchain.chat_models import init_chat_model
# Importa el módulo para manejar variables de entorno
import os

# Configura la clave de API de Google para acceder al modelo Gemini
os.environ["GOOGLE_API_KEY"] = "tu_api_key_aqui"

# Se inicializan los modelos de cada agente
classisifier_model = init_chat_model(
    "gemini-2.5-flash-lite",
    model_provider="google_genai",
    temperature=0
)
publications_model = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai",
    temperature=1
)
complaints_model = init_chat_model(
    "gemini-2.5-pro",
    model_provider="google_genai",
    temperature=1
)
general_model = init_chat_model(
    "gemini-2.0-flash",
    model_provider="google_genai",
    temperature=1.5
)


def classify_message(user_message: str) -> str:
    """
    Clasifica el mensaje del usuario para determinar el tipo de consulta con ayuda de un modelo de IA.

    Args:
        user_message (str): Mensaje del usuario a clasificar.

    Returns:
        str: Tipo de consulta clasificado.
    """
    try:
        print("Ingrsando al clasificador de mensajes...")
        # Define el mensaje de sistema para guiar al modelo
        system_message = {
            "role": "system",
            "content": (
                """
                Sos un asistente que clasifica mensajes en 3 categorías: publicaciones, reclamos y otros.\n"
                "Tenes que analizar el mensaje del usuario y devolver una sola palabra que indique la categoría.\n"
                "Las categorías son: 'publicacion', 'reclamo' y 'otro'.
                "Cuando el usuario no pide vender un producto o hacer un reclamo, SIEMPRE debes devolver 'otro'.\n"
                """
            )
        }

        messages = [
            system_message,
            {"role": "user", "content": user_message}
        ]

        # Invoca el modelo de clasificación con el mensaje del usuario
        response = classisifier_model.invoke(messages)

        # Devuelve la categoría clasificada
        return response.content.strip()
    except Exception as e:
        return f"[Error al clasificar mensaje: {e}]"


def get_agent_config(category: str) -> tuple:
    """
    Selecciona el modelo de IA a utilizar y sus instrucciones según la categoría del mensaje inicial.

    Args:
        category (str): Categoría del mensaje ('publicacion', 'reclamo', 'otro').

    Returns:
        tuple: Modelo de IA y mensaje de sistema con instrucciones.
    """
    print("Seleccionando configuración del agente...")
    
    if category == "publicacion":
        model_name = "publications_model"
        model = publications_model
        instructions = {
            "role": "system",
            "content": (
                """
                Sos un asistente de ventas que ayuda a los usuarios a publicar y vender sus productos.\n"
                "Tenes que tener un tono amigable y usar emojis en tus respuestas."
                """
            )
        }
    elif category == "reclamo":
        model_name = "complaints_model"
        model = complaints_model
        instructions = {
            "role": "system",
            "content": (
                """
                Sos un asistente que maneja reclamos de clientes de manera profesional y empática.\n"
                "Tenes que disculparte por los inconvenientes y ofrecer soluciones adecuadas."
                """
            )
        }
    else:
        model_name = "general_model"
        model = general_model
        instructions = {
            "role": "system",
            "content": (
                """
                Tu funcion es transmitir a los usuarios que no podes ayudarlos con su consulta.\n"
                "Debes decirle que por ahora solo podes ayudarlos a vender sus productos o con reclamos.\n"
                "Tenes que tener un tono amigable y usar emojis en tus respuestas."
                """
            )
        }
    print(f"Configuración del agente seleccionada. Modelo: {model_name}")
    return model, instructions


def get_response(messages: list[dict]) -> list[dict]:
    """
    Funcion que decice que asistente utilizar y devuelve una respuesta al usuario.
    Args:
        messages (list[dict]): Lista de mensajes en formato dict, cada uno con 'role' y 'content'.
    Returns:
        list[dict]: Lista de mensajes incluyendo la respuesta del asistente.
    """

    # Se evalua el primer mensaje del usuario para clasificar el tipo de consulta
    category = classify_message(messages[0]["content"])
    print(f"Categoría clasificada: {category}")
    
    # Se obtiene el modelo y las instrucciones del agente según la categoría
    model, system_message = get_agent_config(category)

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
