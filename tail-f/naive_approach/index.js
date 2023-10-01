const socket = new WebSocket('ws://localhost:8000'); // Change the URL as needed

socket.addEventListener('open', (event) => {
    console.log('WebSocket connection opened:', event);
});

socket.addEventListener('message', (event) => {
    console.log('WebSocket message received:', event);
    updatePage(event.data);
});

socket.addEventListener('close', (event) => {
    console.log('WebSocket connection closed:', event);
});

socket.addEventListener('error', (event) => {
    console.error('WebSocket error:', event);
});

function updatePage(data) {
    const websocketDataDiv = document.getElementById('websocket-data');
    websocketDataDiv.textContent = `Received data: ${data}`;
}