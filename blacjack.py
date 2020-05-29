# Assign cards and further add it in deck

import random

suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','King','Queen','Jack','Ace')
values={'One':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'King':10,'Queen':10,'Jack':10,'Ace':11}

playing=True

# To print value of specific card

class Card():
	
	def __init__(self,rank,suit):
		self.rank=rank
		self.suit=suit

	def __str__(self):
		return self.rank + ' of ' + self.suit

# to add cards in deck

class Deck():
	
	def __init__(self):
		self.deck=[]
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp=' '
		for card in self.deck:
			deck_comp+='\n '+card.__str__()
			return 'The Deck has:'+deck_comp

# to shuffle deck	
	def shuffle(self):
		random.shuffle(self.deck)
		
# to pop out single card
	def deal(self):
		single_Card=self.deck.pop()
		return single_Card

# To add values of card

class Hand():

	def __init__(self):
		self.cards=[]
		self.value=0
		self.aces=0

	def add_cards(self,card):
		self.cards.append(card)
		self.value+=values[card.ranks]
		if code.rank=='Ace':
			self.aces+=1

	def adjust_for_ace(self):
		if self.value>21 and self.aces>0:
			self.value-=10
			self.aces-=1