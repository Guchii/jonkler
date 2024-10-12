import pydealer as pd
class Player:
    def __init__(self, name):
        self.name = name
        self.hand: pd.Stack = None

    def hand_values(self):
        return {card.value for card in self.hand}