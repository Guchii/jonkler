from game import Game
import json
import asyncio
from icecream import ic

class SocketManager:
    def __init__(self):
        self.connections = {}

    async def connect(self, websocket, room):
        await websocket.accept()
        if self.connections.get(room) is None:
            self.connections[room] = {"connections": []}
        self.connections[room]['connections'].append(websocket)


    async def send_message(self, room, message):
        for connection in self.connections[room]["connections"]:
            await connection.send_json(message)
    
    async def send_user_event(self, room, event):
        connections = self.connections[room]["connections"]
        turn = event.get("uid") - 1
        for idx, conn in enumerate(connections):
            if idx == turn:
                await conn.send_json(event)
            else:
                event["plays"] = []
                await conn.send_json(event)

    async def game_actions(self, room, event):
        ic(self.connections[room])
        event = json.loads(event)

        if event["event"] == "create":
            game = Game(event["user"], event["id"])
            self.connections[room]['game'] = game
            await self.send_message(room, {"event": "created"})
        
        
        elif event["event"] == "join":
            await self.connections[room]['game'].join_game(event)
            await self.send_message(room, {"event": "joined", "user": event["user"]})


        elif event["event"] == "start":
            updated_event = await self.connections[room]['game'].start_game()
            await self.send_user_event(room, updated_event)


        else:
            game = room['game']
            updated_event = await game.handle_event(event)
