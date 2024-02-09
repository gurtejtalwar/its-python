import asyncio
import websockets

async def hello(websockets):
    name = await websockets.recv()
    print(f"Server Received: {name}")

    greeting = f"Hello {name}!"

    await websockets.send(greeting)
    print(f"Server Sent: {greeting}")

async def start_server():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever
    
if __name__ == "__main__":
    asyncio.run(start_server())