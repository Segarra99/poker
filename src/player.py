from .hand import Hand

class Player:
  def __init__(self, name):
    self.name = name
    self.chips = 50
    self.hand = Hand()
    self.folded = False

  def show_hand(self):
    print(f"{self.name}'s hand:")
    for card in self.hand.cards:
      print(f"{card.value} of {card.suit}")

  def bet(self, amount):
    if amount > self.chips:
      print("Not enough chips!")
      return
    self.chips -= amount
    print(f"{self.name} bets {amount} chips.")

  def call(self, amount):
    self.chips -= amount
    print(f"{self.name} calls.")

  def fold(self):
    self.folded = True
    print(f"{self.name} folds.")

  def reveal(self):
    print(f"{self.name} has {self.hand.cards[0].value} of {self.hand.cards[0].suit} and {self.hand.cards[1].value} of {self.hand.cards[1].suit}.")