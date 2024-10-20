from icecream import ic
class Game:




    async def playturn():
        pass
    async def passturn():
        pass
    async def callbluff():
        pass

    def __init__(self, owner, uid) -> None:
        self.owner = owner
        self.players = [(owner, uid)]
        self.plays = {
            "playturn": self.playturn,
            "passturn": self.passturn,
            "callbluff": self.callbluff,
        }
        return None

    async def join_game(self, event):
        self.players.append((event["user"], event["id"]))
        ic(self.players)
        return None

    async def handle_event(self, event):
        action = event.get("player_action")
        run_action = self.plays.get(action, None)
        if run_action:
            await run_action(event)
    
    async def start_game(self):
        self.turn = 0
        user, uid = self.players[self.turn]

        event = {
            "turn": user,
            "uid": uid,
            "plays": list(self.plays.keys())
        }
        return event

