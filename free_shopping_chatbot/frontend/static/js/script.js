

const messagesDiv = document.getElementById('messages');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

let messages = [];

function renderMessages() {
    messagesDiv.innerHTML = '';
    messages.forEach(msg => {
        const div = document.createElement('div');
        if (msg.role === 'user') {
            div.textContent = `Tú: ${msg.content}`;
        } else if (msg.role === 'assistant') {
            div.textContent = `Bot: ${msg.content}`;
        } else {
            div.textContent = `${msg.role}: ${msg.content}`;
        }
        div.style.marginBottom = '8px';
        messagesDiv.appendChild(div);
    });
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

chatForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    const text = userInput.value.trim();
    if (text) {
        // Agregar mensaje del usuario al historial
        messages.push({ role: 'user', content: text });
        renderMessages();
        userInput.value = '';
        try {
            const response = await fetch('http://localhost:8000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ messages })
            });
            const data = await response.json();
            if (Array.isArray(data.reply)) {
                messages = data.reply;
                renderMessages();
            } else {
                // Si hay error, mostrarlo como mensaje del bot
                messages.push({ role: 'assistant', content: data.reply });
                renderMessages();
            }
        } catch (error) {
            messages.push({ role: 'assistant', content: 'Error de conexión con el servidor.' });
            renderMessages();
        }
    }
});
