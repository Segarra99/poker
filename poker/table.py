from .deck import Deck

class Table:
  def __init__(self):
    self.players = []
    self.deck = Deck()
    self.board = []

  def add_player(self, player):
    self.players.append(player)

  def deal(self):
    for player in self.players:
      player.deck.deal(player)

  