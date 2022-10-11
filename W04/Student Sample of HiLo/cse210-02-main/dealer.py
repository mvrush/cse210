from deck import Deck
from player import Player

#Giving the game some flare with color pops.
class textColors:
	RED = '\u001b[31m'
	GREEN = '\u001b[32m'
	CYAN = '\u001b[36m'
	MAGENTA = '\u001b[35m'
	WHITE = '\u001b[37m'

class Dealer:
	def __init__(self):
		self.is_playing = True
		self.total_score = 0
		self.deck = Deck()
		self.players = []
		self.winning_score = 1000
		self.active_player = None

	def draw(self,deck):
		self.hand.append(deck.draw_card())

	def start_game(self):
		deal_cards = input(textColors.GREEN + "Ready to try your luck?[y/n]" + textColors.WHITE)
		self.is_playing = (deal_cards == "y")
		self.deck.create_deck()
		self.deck.shuffle()
		num_players = int(input(textColors.MAGENTA + "How many players?"))
		for player in range(num_players):
			player = Player(debug=False)
			player.get_name()
			self.players.append(player)
		self.active_player = player
		self.winning_score = int(input(textColors.MAGENTA + f"Hello, what score would you like to play to? " + textColors.WHITE))

		while self.is_playing:
			for player in self.players:
				self.get_inputs()
				self.update_game(player)
				self.output_results(player)

	def get_inputs(self):
		pass

	def reshuffle(self):
		"""If self.deck.cards runs out of cards:
		 creates a new deck
		  and randomizes the array"""
		if len(self.deck.cards) == 0:
			self.deck.create_deck()
			self.deck.shuffle()

	def update_game(self,player):
		""" controls the flow of the game
		enforces rule sets 
		and determines the point values of player.guess
		"""
		if not self.is_playing:
			print(textColors.RED + "Thanks for playing!\nCome again!" + textColors.WHITE)
			return
		
		self.reshuffle()
		if len(player.hand) == 0:
			first_card = self.deck.draw_card()
			player.hand.append(first_card)
		print(textColors.MAGENTA + f"The card is a {player.get_current_card().value} of {player.get_current_card().suit}" + textColors.WHITE)
		guess = player.get_guess()

		print(f"You chose {guess}")
		next_card = self.deck.draw_card()
		print(f"You Drew a {next_card.value} of {next_card.suit}")
		if guess.lower() == "h":
			if next_card >= player.get_current_card():
				print(textColors.GREEN + "You were correct!" + textColors.WHITE)
				player.score += 100
			else:
				print (textColors.RED + "Sorry, you guessed wrong" + textColors.WHITE)
				player.score -= 75
		elif guess.lower() == "l":
			if next_card < player.get_current_card():
				print(textColors.GREEN + "You were correct!" + textColors.WHITE)
				player.score += 100
			else:
				print(textColors.RED + "Sorry, you guessed wrong" + textColors.WHITE)
				player.score -= 75

		player.hand[0] = next_card

	def output_results(self,player):
		"""
		Outputs each player's current score
		Decides winning/losing score
		removes player once they win or lose
		"""
		if not self.is_playing:
			return

		print(f"Your current score is {player.score}")
		
		if player.score <= 0:
			print(textColors.RED + f"Sorry {player.name}, but the house always wins...MWAHAHAHA" + textColors.WHITE)
			self.players.remove(player)

		elif player.score >= self.winning_score:
			print(textColors.GREEN + f"{player.name} You are a winner!!!" + textColors.WHITE)
			self.players.remove(player)
		if len(self.players) == 0:
			self.is_playing = False


