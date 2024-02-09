import websockets
import asyncio 
import keyboard # listen to keyboard events

# start websocket client
async def start_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        done = False
        while not done:
            if keyboard.is_pressed('b'):
                await websocket.send("buzz")
                print(f"Client Sent: buzz")
                response = await websocket.recv()
                print(f"Client Received: {response}")