from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from socket_manager import SocketManager

app = FastAPI()
socket = SocketManager() 


@app.websocket("/ws/{room}")
async def websocket_endpoint(websocket: WebSocket, room: str):
    await socket.connect(websocket, room)
    try:
        while True:
            await socket.game_actions(room, await websocket.receive_text())

    except WebSocketDisconnect:
        socket.connections[room]['connections'].remove(websocket)
        del websocket

@app.get("/")
async def get():
    return "Hello World"