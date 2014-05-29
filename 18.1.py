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

c = Card(2, 11)
print c
