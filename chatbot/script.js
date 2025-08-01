const chatWindow = document.getElementById('chat-window');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

const respuestasBot = [
    {
        keywords: ['comprar', 'venta', 'producto', 'precio'],
        respuesta: 'Para comprar un producto, selecciona el artículo deseado y sigue el proceso de pago. ¿Te gustaría saber más sobre algún producto en particular?'
    },
    {
        keywords: ['devolución', 'devolver', 'reembolso', 'cambiar'],
        respuesta: 'Para realizar una devolución, debes solicitarla dentro de los 30 días posteriores a la compra. ¿Necesitas ayuda con una devolución específica?'
    },
    {
        keywords: ['envío', 'entrega', 'llegar', 'demora'],
        respuesta: 'El envío suele tardar entre 2 y 5 días hábiles. Puedes rastrear tu pedido desde tu cuenta.'
    },
    {
        keywords: ['ayuda', 'soporte', 'contacto'],
        respuesta: 'Puedes contactarnos por chat, email o teléfono. ¿En qué podemos ayudarte hoy?'
    }
];

function agregarMensaje(texto, clase) {
    const msg = document.createElement('div');
    msg.className = `message ${clase}`;
    msg.textContent = texto;
    chatWindow.appendChild(msg);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function obtenerRespuesta(pregunta) {
    const preguntaLower = pregunta.toLowerCase();
    for (const item of respuestasBot) {
        if (item.keywords.some(k => preguntaLower.includes(k))) {
            return item.respuesta;
        }
    }
    return 'Lo siento, ¿podrías darme más detalles sobre tu consulta de ventas o devoluciones?';
}

chatForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const pregunta = userInput.value.trim();
    if (!pregunta) return;
    agregarMensaje(pregunta, 'user');
    setTimeout(() => {
        const respuesta = obtenerRespuesta(pregunta);
        agregarMensaje(respuesta, 'bot');
    }, 500);
    userInput.value = '';
});

// Mensaje de bienvenida
agregarMensaje('¡Hola! Soy tu asistente para ventas y devoluciones. ¿En qué puedo ayudarte?', 'bot');
