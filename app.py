import random
from table import Table
from player import Player
games = []

def start_game(table: Table) -> None:
    print(f"Game started by {table.owner}")
    print(f"Players: {table.players}")
    print(f"Number of players: {table.curr_players}")


    table.deal_cards()
    table.make_play()

users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
players = random.sample(users, 4)
players = [Player(player) for player in players]
owner = random.choice(players)

table = Table(owner)
table.curr_players = len(players)

table.set_table(players)
start_game(table)