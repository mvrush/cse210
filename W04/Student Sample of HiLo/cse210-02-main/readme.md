### This is the "team d" hilo game. 
- [Purpose of the Project](#purpose-of-the-project)
- [Game Rules](#game-rules)
- [Object and Class documentaion](#object-and-class-documentaion)

# Student check-in 
Tukker De Hart  

# Purpose of the Project

To learn together the principles of abstraction. Meanwhile practicing using Version Control Systems to keep colabrative code organized. 

# Game Rules

    The player starts the game with 300 points.
    Individual cards are represented as a number from 1 to 13.
    The current card is displayed.
    The player guesses if the next one will be higher or lower.
    The the next card is displayed.
    The player earns 100 points if they guessed correctly.
    The player loses 75 points if they guessed incorrectly.
    If a player reaches 0 points the game is over.
    If a player has more than 0 points they decide if they want to keep playing.
    If a player decides not to play again the game is over.

# Object and Class documentaion

At least two classes
	Player 
		Properties:
			score
			name
            debug
		Methods:
			make guess
				returns String H or L
                debug mode skips input and alternates between H or L
			get_name

	Dealer
		Draw the card -- calls the get card function
		Enforce rules -- hi/lo and score
		Control flow
			Ask Player
			Display cards
			
	Deck

		Properties: 
			Cards - array
		Fucntions:
			create_cards -- Loop through and populate the Cards array
			draw_card -- get a card from the Cards[] and return it
			*shuffle  -- rearragne the Cards[]
			
	Cards
		Properties:
			Number
			Suit
		
		
