import pydealer as pd

def get_new_deck():
    deck = pd.Deck()
    deck.shuffle()
    return deck
