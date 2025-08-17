# Clase 7: Uso de agentes de IA en el chatbot

## Resumen de los cambios recientes en `chatbot_service.py`

En esta clase se implementó una arquitectura basada en agentes de IA para el chatbot de Free Shopping. El objetivo es que el sistema pueda identificar la intención del usuario y responder de manera especializada según el tipo de consulta.

### ¿Cómo funciona?

1. **Evaluación de la intención del usuario**
   - El primer mensaje del usuario se analiza usando un modelo de clasificación (`classisifier_model`).
   - El modelo determina si la consulta corresponde a una de estas categorías: `publicacion`, `reclamo` u `otro`.

2. **Selección del agente adecuado**
   - Según la categoría detectada, se selecciona el agente (modelo de IA) más apropiado:
     - **publicacion**: Asistente de ventas, ayuda a publicar y vender productos.
     - **reclamo**: Asistente de atención al cliente que maneja reclamos de forma profesional y empática.
     - **otro**: Asistente general, informa al usuario cuando no puede ayudarlo con su consulta.

3. **Configuración personalizada**
   - Cada agente tiene instrucciones de sistema específicas para adaptar el tono y el tipo de respuesta.
   - Por ejemplo, el agente de ventas usa emojis y un tono amigable, mientras que el de reclamos es empático y profesional.

4. **Flujo de la conversación**
   - El mensaje de sistema se inserta al inicio de la conversación.
   - El modelo genera la respuesta y se agrega a la lista de mensajes.
   - El mensaje de sistema se elimina antes de devolver la conversación al frontend.

### Ventajas de este enfoque
- Permite respuestas más precisas y útiles para cada tipo de consulta.
- Facilita la escalabilidad y el mantenimiento del chatbot.
- Mejora la experiencia del usuario al recibir atención especializada.

---

## Cambios recientes
Los últimos cambios realizados en el proyecto pueden verse en el siguiente commit:
[Ver commit en GitHub](https://github.com/martin-paladino/ia-para-programadores-jul-25/commit/da3fcb845b53a29e2934ffa44845a2e2f529290f)

## Recursos útiles para mejorar y escalar el servicio

### LangGraph
[¿Por qué usar LangGraph?](https://langchain-ai.github.io/langgraph/concepts/why-langgraph/)
LangGraph es una librería que permite crear flujos de agentes y cadenas de manera flexible y escalable. Es ideal para sistemas complejos de IA conversacional, ya que facilita la orquestación de múltiples agentes, la gestión de estados y la integración de herramientas externas. Usar LangGraph puede ayudarte a construir chatbots más robustos y adaptables, capaces de manejar conversaciones avanzadas y tareas especializadas.

### Structured Output en LangChain
[Structured Output en LangChain](https://python.langchain.com/docs/how_to/structured_output/)
El método `with_structured_output` de LangChain permite que los modelos devuelvan respuestas en formatos estructurados, como JSON, en vez de texto libre. Esto es especialmente útil para procesar la respuesta programáticamente, garantizar un formato consistente y facilitar la integración con otros sistemas. En el caso del classifier, permite devolver la categoría detectada de forma estructurada y confiable, mejorando la calidad y utilidad de las respuestas del asistente.
