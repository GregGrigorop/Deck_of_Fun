class Card:
	def __init__(self):
		import random as r
		self.suit = r.choice(['Hearts','Diamonds','Spades','Clubs'])
		self.value = r.choice(['A','2','3','4','5','6','7','8','9','10','J','Q','K'])

	def __repr__(self):
		return f"{self.value} of {self.suit}"

c = Card()
print(c.suit)
print(c.value)
print(c)

class Deck:

	def __init__(self):
		self.cards = [f"{i} of {j}" for i in ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] for j in \
	       ['Hearts','Diamonds','Spades','Clubs']]
	    
	def count(self):
		return len(self.cards)

	def __repr__(self):
		return f"Deck of {self.count()} cards" #OR: return f"Deck of {len(self.cards)} cards" but I have
											   # defined count() already
	def _deal(self,num):
		if self.count() >= num:
			dealt = []
			for i in range(num):
				card = self.cards.pop()
				dealt.append(card)
			return dealt
		else:
			dealt = []
			for i in range(self.count()):
				dealt.append(self.cards.pop())
			print(dealt) # I added this print to see the dealt cards before the ValueError is raised
			raise ValueError("All cards have been dealt")

	def shuffle(self):
		from random import shuffle
		if self.count() == 52:
			return shuffle(self.cards)
		else:
			raise ValueError("Only full decks can be shuffled")

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self,num):
		return self._deal(num)
# OR: return [print(items) for items in self._deal(num)] - to print the list's elements w/o quotes, vertically

# d = Deck()
# print(d.count())
# print(d)
# d.shuffle()
# print(d.cards)
# print(d.deal_card())
# print(d.count())
# print(d.deal_hand(5))
# print(d.count())
# print(d.cards)
# print(d.deal_hand(6))
# print(d)
# print(d.deal_hand(41)) # - check the ValueError if this is run
# d.shuffle()
