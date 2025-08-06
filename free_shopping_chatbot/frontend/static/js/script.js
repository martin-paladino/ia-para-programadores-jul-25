
const messagesDiv = document.getElementById('messages');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

function addMessage(text, sender = 'usuario') {
    const msg = document.createElement('div');
    msg.textContent = sender === 'usuario' ? `Tú: ${text}` : `Bot: ${text}`;
    msg.style.marginBottom = '8px';
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

chatForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    const text = userInput.value.trim();
    if (text) {
        addMessage(text, 'usuario');
        userInput.value = '';
        try {
            const response = await fetch('http://localhost:8000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: text })
            });
            const data = await response.json();
            addMessage(data.reply, 'bot');
        } catch (error) {
            addMessage('Error de conexión con el servidor.', 'bot');
        }
    }
});
