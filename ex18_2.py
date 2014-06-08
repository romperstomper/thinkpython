import random

class Card(object):
  """Represents a standard playing card."""
  suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']
  def __init__(self, suit=0, rank=2):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return ('   ' + self.rank_names[self.rank] + ' of ' + 
            self.suit_names[self.suit])

  def __cmp__(self, other):
    """Determines which of 2 cards is greater.
    Args:
      other: (object) Card to compare.

    Returns:
       1 (int) if self is greater than other 
       -1 (int) if other is greater than self 
       0  (int) if the cards are equal
    """
    t1 = self.suit, self.rank
    t2 = other.suit, other.rank
    return cmp(t1, t2)


class Deck(object):
  """Represents a Deck object which is a list of 52 card objects."""
  def __init__(self):
    self.cards = []
    for suit in range(4):
      for rank in range(1, 14):
        card = Card(suit, rank)
        self.cards.append(card)

  def __str__(self):
    """String representation of the deck.
    Returns:
      res: (str) One continuous string, 1 card per line.
    """
    res = []
    for card in self.cards:
      res.append(str(card))
    return '\n'.join(res)

  def pop_card(self):
    """Remove the last card from the deck.
    
    Returns:
      Card: (str) Bottom card of the deck
    """  
    return self.cards.pop()

  def add_card(self, card):
    """Adds a card to the deck.
    
      Args:
        Card: (str) Card string to be append to the Deck.
    """
    self.cards.append(card)
    
  def shuffle(self):
    """Mix the order of the cards in the deck to randomize the cards."""
    random.shuffle(self.cards)

  def sort(self):
    """Sorts the cards in a Deck."""
    self.cards.sort()
    pass

a = Deck()
print a
a.shuffle()
print a
a.sort()
print a 
