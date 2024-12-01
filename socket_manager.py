from game import Game
import json
import asyncio
from icecream import ic

class SocketManager:
    def __init__(self):
        self.connections = {}

    async def connect(self, websocket, room):
        print("accepting new connection")
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
        print("current connections", self.connections)
        event = json.loads(event)
        ic(event)

        # Get the game state requested by the user
        user_rq_stae = event.get("user_rq_state")

        if  user_rq_stae == "create":
            user_rq_game = Game(event["user"], event["id"])
    
            self.connections[room]['game'] = user_rq_game
            await self.send_message(room, {"event": "created"})
        
        
        elif user_rq_stae == "join":
            await self.connections[room]['game'].join_game(event)
            await self.send_message(room, {"event": "joined", "user": event["user"]})


        elif user_rq_stae == "start":
            updated_event = await self.connections[room]['game'].start_game()
            await self.send_user_event(room, updated_event)
        
        elif user_rq_stae == "action":
            ...
        
        else:
            await self.send_message(room, {"error": "Invalid request"})
            return None


