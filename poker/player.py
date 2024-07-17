class Player:
  def __init__(self, name):
    self.name = name
    self.chips = 50
    self.hand = []

  def show_hand(self):
    print(f"{self.name}'s hand:")
    for card in self.hand:
      print(f"{card.value} of {card.suit}")