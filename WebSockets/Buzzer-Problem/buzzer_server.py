import asyncio 
import websockets

clients = []

async def handle_message(websocket, path):
    global clients
    global fastest_time
    message = await websocket.recv()
    if message == "buzz":
        response_time = asyncio.get_event_loop().time() 
        clients.append([websocket, response_time])
        if len(clients) == 1:
            await websocket.send("You buzzed in first!")
            fastest_time = response_time
        else:
            t = round(fastest_time - response_time, 2)
            await websocket.send(f"You buzzed in {t} seconds after the first person")

async def start_server():
    async with websockets.serve(handle_message, "localhost", 8765):
        await asyncio.Future()  # run forever   

if __name__ == "__main__":
    asyncio.run(start_server())