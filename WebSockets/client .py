import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"Client Sent: {name}")

        greeting = await websocket.recv()
        print(f"Client Received: {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())