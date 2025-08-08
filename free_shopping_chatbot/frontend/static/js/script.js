

const messagesDiv = document.getElementById('messages');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const loader = document.getElementById('loader');

let messages = [];

function renderMessages() {
    messagesDiv.innerHTML = '';
    messages.forEach(msg => {
        const div = document.createElement('div');
        let htmlContent = marked.parse(msg.content || '');
        if (msg.role === 'user') {
            div.className = 'msg-chip msg-user';
            div.innerHTML = htmlContent;
        } else if (msg.role === 'assistant') {
            div.className = 'msg-chip msg-bot';
            div.innerHTML = htmlContent;
        } else {
            div.className = 'msg-chip';
            div.innerHTML = marked.parse(`${msg.role}: ${msg.content}`);
        }
        messagesDiv.appendChild(div);
    });
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

chatForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    const text = userInput.value.trim();
    if (text) {
        messages.push({ role: 'user', content: text });
        renderMessages();
        userInput.value = '';
        loader.style.display = 'flex';
        try {
            const response = await fetch('http://localhost:8000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ messages })
            });
            const data = await response.json();
            loader.style.display = 'none';
            if (Array.isArray(data.reply)) {
                messages = data.reply;
                renderMessages();
            } else {
                messages.push({ role: 'assistant', content: data.reply });
                renderMessages();
            }
        } catch (error) {
            loader.style.display = 'none';
            messages.push({ role: 'assistant', content: 'Error de conexión con el servidor.' });
            renderMessages();
        }
    }
});
