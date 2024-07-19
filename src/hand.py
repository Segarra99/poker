class Hand:
  def __init__(self):
    self.cards = []

  def add_card(self, card):
    self.cards.append(card)

  def get_combo(self, board):
    all_cards = self.cards + board

    if self.is_royal_flush(all_cards):
      return "Royal Flush"
    elif self.is_straight_flush(all_cards):
      return "Straight Flush"
    elif self.is_four_of_a_kind(all_cards):
      return "Four of a Kind"
    elif self.is_full_house(all_cards):
      return "Full House"
    elif self.is_flush(all_cards):
      return "Flush"
    elif self.is_straight(all_cards):
      return "Straight"
    elif self.is_three_of_a_kind(all_cards):
      return "Three of a Kind"
    elif self.is_two_pairs(all_cards):
      return "Two Pairs"
    elif self.is_one_pair(all_cards):
      return "One Pair"
    else:
      return "High Card"
    
  def get_high_card(cards):
    value_map = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for card in cards:
        if card.value in value_map:
            card.value = value_map[card.value]
            
    highest_card = max(cards, key=lambda card: card.value)
    return highest_card.value

  def is_royal_flush(cards):
    if len(cards) < 5:
      return False
    
    same_suit = all(card.suit == cards[0].suit for card in cards)
    if not same_suit:
      return False
    
    has_ace = any(card.value == 'A' for card in cards)
    if not has_ace:
      return False
    
    has_king = any(card.value == 'K' for card in cards)
    if not has_king:
      return False
    
    has_queen = any(card.value == 'Q' for card in cards)
    if not has_queen:
      return False
    
    has_jack = any(card.value == 'J' for card in cards)
    if not has_jack:
      return False
    
    has_ten = any(card.value == '10' for card in cards)
    if not has_ten:
      return False
    
    return True
  
  def is_straight_flush(cards):
    if len(cards) < 5:
      return False

    same_suit = all(card.suit == cards[0].suit for card in cards)
    if not same_suit:
      return False
    
    value_map = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for card in cards:
        if card.value in value_map:
            card.value = value_map[card.value]

    cards.sort(key=lambda card: card.value)

    for i in range(len(cards) - 1):
      if cards[i].value + 1 != cards[i + 1].value:
        return False
    
    return True

  def is_four_of_a_kind(cards):
    if len(cards) < 4:
      return False
    
    for card in cards:
      count = 0
      for c in cards:
        if c.value == card.value:
          count += 1
          if count == 4:
            return True
    
    return False

  def is_full_house(cards):
    if len(cards) < 5:
      return False
    
    pair = False
    three_of_a_kind = False
    for card in cards:
      count = 0
      for c in cards:
        if c.value == card.value:
          count += 1
          if count == 2:
            pair = True
          elif count == 3:
            three_of_a_kind = True
            break
    
      if pair and three_of_a_kind:
        return True

    return False
  
  def is_flush(cards):
    if len(cards) < 5:
      return False
    
    for card in cards:
      count = 0
      for c in cards:
        if c.suit == card.suit:
          count += 1
          if count == 5:
            return True
    
    return False
  
  def is_straight(cards):
    if len(cards) < 5:
      return False
    
    value_map = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for card in cards:
        if card.value in value_map:
            card.value = value_map[card.value]

    cards.sort(key=lambda card: card.value)

    count = 1
    for i in range(len(cards) - 1):
      if cards[i].value + 1 == cards[i + 1].value:
        count += 1
      else:
        count = 1
      
      if count == 5:
        return True
    
    return False
  
  def is_three_of_a_kind(cards):
    for card in cards:
      count = 0
      for c in cards:
        if c.value == card.value:
          count += 1
          if count == 3:
            return True
    
    return False
  
  def is_two_pair(cards):
    if len(cards) < 4:
      return False
    
    value_count = {}
    for card in cards:
        if card.value in value_count:
            value_count[card.value] += 1
        else:
            value_count[card.value] = 1
    
    pairs = 0
    for count in value_count.values():
        if count >= 2:
            pairs += 1
    
    return pairs >= 2
  
  def is_one_pair(cards):
    for card in cards:
      count = 0
      for c in cards:
        if c.value == card.value:
          count += 1
          if count == 2:
            return True
    
    return False