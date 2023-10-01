import asyncio
import websockets

HOST = "localhost"
PORT = 8000
current_positions = {}

async def echo_server(websocket, path): 
    current_positions[websocket] = 0
    while True:
        try:
            await websocket.send((await read_file_line_by_line(websocket)).decode("utf-8"))
            await asyncio.sleep(0.7)
        except websockets.exceptions.ConnectionClosedError:
            break

async def read_file_line_by_line(websocket):
    global current_positions
    current_position = current_positions.get(websocket, 0)
    with open("index.log", "rb+") as f:
        f.seek(current_position)
        bytes = f.readline()
        if bytes:
            current_position = f.tell()
            current_positions[websocket] = current_position
        return bytes

start_server = websockets.serve(echo_server, HOST, PORT)
asyncio.get_event_loop().run_until_complete(start_server)
print(f"Listening on {HOST}:{PORT}")
asyncio.get_event_loop().run_forever()