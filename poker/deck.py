from .card import Card

class Deck:
  def __init__(self):
    self.cards = []
    
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    for suit in suits:
      for value in values:
        self.cards.append(Card(suit, value))

  def shuffle(self):
    import random
    random.shuffle(self.cards)

  def deal(self, player):
    player.add_card(self.cards.pop())

  def add_to_board(self, table):
    table.board.add_card(self.cards.pop())