# Clase 3: Herramientas Avanzadas para Desarrollo con IA

En esta clase comenzamos a interactuar con gemini desde su api y desde langchain, creando una interfaz simple para enviar mensajes y ver la respuesta del modelo.

## LangChain

[LangChain](https://python.langchain.com/docs/tutorials/) es un framework para desarrollar aplicaciones potenciadas por modelos de lenguaje (LLMs) que facilita:

- Interacción con diferentes modelos de lenguaje
- Creación de cadenas para procesar datos secuencialmente
- Integración con bases de datos y fuentes de conocimiento externas
- Implementación de memoria para mantener contexto en conversaciones
- Creación de agentes que pueden tomar decisiones y usar herramientas

LangChain proporciona abstracciones que simplifican el desarrollo de aplicaciones complejas con LLMs, permitiéndote centrarte en la lógica de negocio en lugar de los detalles de implementación.

## Proyecto Chatbot: Concepto y Arquitectura

El proyecto que estamos desarrollando es un chatbot inteligente que puede:
- Recibir mensajes de los usuarios
- Determinar la intención del usuario: vender un productor, hacer un reclamo u otro.
- Dirigir la consulta al agente apropiado según la intención detectada

A continuación se muestra el flujo de trabajo del sistema:

![Arquitectura del chatbot](/recursos/imagenes/agentes.png)

### Agentes en IA

Los [agentes](https://www.kaggle.com/whitepaper-agents) son componentes autónomos de software con capacidades específicas:

- Cada agente tiene instrucciones específicas y un propósito definido
- Pueden utilizar diferentes modelos de lenguaje según sus necesidades
- Tienen la capacidad de tomar decisiones basadas en información
- Pueden interactuar con personas, otros agentes o herramientas externas
- Actúan como expertos en un dominio específico dentro del sistema

En nuestro chatbot, implementamos tres agentes principales:
1. **Agente 1**: Determina la intención del usuario
2. **Agente 2**: Especializado en ayudar a publicar productos
3. **Agente 3**: Especializado en ayudar con reclamos del usuario


## Herramientas y Recursos Adicionales

## Cursor IDE

[Cursor](https://www.cursor.com/) es un editor de código diseñado específicamente para trabajar con IA, que ofrece:

- Asistencia de código en tiempo real con modelos avanzados de IA
- Capacidad para entender tu codebase completo
- Edición de código mediante lenguaje natural
- Interfaz familiar basada en VS Code (puedes importar extensiones, temas y atajos)
- Opciones de privacidad para proteger tu código

Cursor permite desarrollar software mucho más rápido gracias a su integración profunda con IA, funcionando como un par programador que comprende el contexto de todo tu proyecto.

### Documentación Complementaria
- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/)
- [Guía de modelos de chat en LangChain](https://python.langchain.com/docs/integrations/chat/)
