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
      if not player.folded:
        player.deck.deal(player)

  def flop(self):
    for _ in range(3):
      self.deck.add_to_board(self)

  def turn(self):
    self.deck.add_to_board(self)

  def river(self):
    self.deck.add_to_board(self)

  def show_board(self):
    print("Board:")
    for card in self.board:
      print(f"{card.value} of {card.suit}")