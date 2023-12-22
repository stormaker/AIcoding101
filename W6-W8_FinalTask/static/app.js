document.addEventListener('DOMContentLoaded', () => {
    const uploadButton = document.getElementById('uploadButton');
    const fileInput = document.getElementById('fileInput');
    const progressBar = document.getElementById('progressBar');
    const ws = new WebSocket('ws://localhost:8000/ws');

    ws.onopen = function(event) {
        console.log("Connected to WebSocket");
    };

    ws.onmessage = function(event) {
        const data = JSON.parse(event.data);
        console.log(data.progress); // 更新进度信息
    };

    ws.onclose = function(event) {
        console.log("Disconnected from WebSocket");
    };

    ws.onerror = function(error) {
        console.log('WebSocket Error: ' + error);
    };

    uploadButton.onclick = function() {
        const file = fileInput.files[0];
        if (file) {
            const formData = new FormData();
            formData.append("file", file);

            fetch('/uploadfile/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => console.log(data.info))
            .catch(error => console.error('Error:', error));
        } else {
            console.log("No file selected");
        }
    };
});
