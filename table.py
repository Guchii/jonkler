import random
import time
import deck
from player import Player
import pydealer as pd

class Table:
    def __init__(self, owner) -> None:
        self.owner = owner
        self.players: Player = [None] * 6
        self.table_id: str = None
        self.table_type: str = None

    def set_curr_players(self, count: int) -> None:
        self._curr_players = count
    
    def get_curr_players(self) -> int:
        return self._curr_players
    
    curr_players = property(get_curr_players, set_curr_players)

    def set_deck(self, deck) -> None:
        self._deck = deck
    
    def get_deck(self):
        return self._deck
    
    tdeck = property(get_deck, set_deck)

    
    def set_table(self, players: list) -> None:
        self.players = players
    
    def deal_cards(self) -> None:
        self.tdeck = deck.get_new_deck()
        for player in self.players:
            if player is None:
                continue
            player.hand = self.tdeck.deal(5)
    def player_show_hand(self, player) -> None:
        print(f"{player.name}'s hand:")
        print(player.hand)
    
    def run_plays(self, play_choice):
        plays = {
            "1": ...
            
        }
    def make_play(self):
        TURN = random.randint(0, self.curr_players - 1)
        self.flush = pd.Stack()
        self.table_pile = pd.Stack()
        self.top, self.bottom = 0, 0

        while True:
            curr_player: Player = self.players[TURN % self.curr_players]
            print(f"{curr_player.name}'s turn")
            self.player_show_hand(self.players[TURN])

            print("Choose a Value to play")
            print(curr_player.hand_values())
            value = input()
            print("Choose cards to play")
            cards = input().split(" ")
            amount = len(cards)
            print(f"Playing {amount} cards of value {value}")
            _played_cards = curr_player.hand.get_list(cards)
            self.table_pile.add(_played_cards)
            print(f"Table Pile: {self.table_pile}")
            self.bottom = self.top
            self.top += amount
            TURN += 1
