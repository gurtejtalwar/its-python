# WebSocket Demp App with FastAPI

## Overview

This is a simple WebSocket application implemented using FastAPI.

## WebSockets

WebSocket is a cross-platform communication protocol between a server and client, that enables bi-directional communication channels over a single, long-lived TCP connection. Unlike traditional HTTP, which follows a request-response model, WebSockets enable real-time, bidirectional communication between clients and servers.

Key features of WebSockets:

- **Full-duplex Communication**: Allows data to be sent and received simultaneously.
  
- **Low Latency**: WebSockets reduce the latency compared to traditional HTTP.

- **Real-time Updates**: Ideal for applications requiring real-time updates, such as chat applications, live notifications, and online gaming.

## Implementation

### FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+. It is designed to be easy to use and efficient, making it an excellent choice for building WebSocket applications.

### Code Structure

- **HTML Template**: The HTML template (`html` variable) includes a simple form for sending messages and a list to display received messages.

- **FastAPI Routes**:
  - `/`: Returns an HTMLResponse with the WebSocket chat interface.
  - `/ws`: WebSocket endpoint for handling WebSocket connections.

- **WebSocket Endpoint** (`websocket_endpoint` function): Accepts WebSocket connections, sends an acknowledgment, and continuously receives and sends messages to/from clients.

- **JavaScript Code**: The JavaScript code in the HTML template establishes a WebSocket connection and handles sending and receiving messages.

### How to Run

1. Install required dependencies:

   ```bash
   pip install fastapi uvicorn
   ```

2. Run the application:

   ```bash
   uvicorn your_app_module_name:app --reload
   ```

   Replace `your_app_module_name` with the name of the file where your FastAPI app is defined.

3. Open a web browser and navigate to `http://localhost:7860` to see the WebSocket chat interface.

4. Type a message in the input field, click "Send," and observe real-time updates in the chat window.

### Dependencies

- **FastAPI**: The main web framework.
- **Uvicorn**: ASGI server used to run the FastAPI application.

### Note

- This is a basic example, and for a production environment, you may need to consider security measures and handle disconnections gracefully.

Feel free to customize the code further based on your application requirements.

Enjoy building real-time applications with FastAPI and WebSockets!