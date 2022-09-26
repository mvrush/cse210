"""
File: tictac.py
Author: Matt Rushton

Purpose: Two players play a game of Tic-Tac-Toe.
Input: Users chooses a spot on a grid to place either and X or an O.
Output: Show users placement on grid and inform when a victory is attained.

"""
print(f"\nWelcome to Tic-Tac-Toe!\nPlayer One will be X's and Player Two will be O's.\nReady Player One?")

# This function will print the grid when called
def print_grid():
    print(f"\n{squares[0]}|{squares[1]}|{squares[2]}\n-+-+-\n{squares[3]}|{squares[4]}|{squares[5]}\n-+-+-\n{squares[6]}|{squares[7]}|{squares[8]}\n")

def main():
    if (squares[0] == squares[1] == squares[2] or
        squares[3] == squares[4] == squares[5] or
        squares[6] == squares[7] == squares[8] or
        squares[0] == squares[3] == squares[6] or
        squares[1] == squares[4] == squares[7] or
        squares[2] == squares[5] == squares[8] or
        squares[0] == squares[4] == squares[8] or
        squares[2] == squares[4] == squares[6]):
        winner = 'yes'
        return winner

winner = ''
turns = 0
squares = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # This is our number array for the grid using strings. If you want integers it would be 1, 2, etc with no ''

print_grid()

# This is the while loop that runs while the 'winner' variable does not equal '!=' 'yes' and the 'turns' variable is less than 9
# We count the turns because if 9 turns are taken, it will be taken on X's turn and the game will be a draw.
while winner != 'yes' and turns < 9:
    number_input = input("X's turn to choose a square (1-9): ") # We use 'int()' to specify that input will be an integer, not a string.
    turns += 1 # adds a turn to the turns counter. When the counter reaches 9, it's a draw.

    # for loop looks at each index position in the length of the squares array using range()
    # It then compares what's in each index position with the number_input and if it matches, replaces it with an X.
    for i in range(len(squares)):
        if squares[i] == number_input:
            squares[i] = 'X'

    print_grid()
    # print(f"Turns = {turns}") # Used for debugging
    winner = main()
    if winner == 'yes':
        print('Player 1 is the winner!')
    elif turns == 9:
        print(f"\nThe game was a draw!")

    if winner != 'yes' and turns < 9: # Using 'if' to run player 2's turn if 'winner' does not '!=' equal 'yes' and turns is less than 9.
        number_input = input("O's turn to choose a square (1-9): ") # We use 'int()' to specify that input will be an integer, not a string.
        turns += 1 # adds a turn to the turns counter. When the counter reaches 9, it's a draw.

        # for loop looks at each index position in the length of the squares array using range()
        # It then compares what's in each index position with the number_input and if it matches, replaces it with an O.
        for i in range(len(squares)):
            if squares[i] == number_input:
                squares[i] = 'O'

        print_grid()
        # print(f"Turns = {turns}") # Used for debugging
        winner = main()
        if winner == 'yes':
            print('Player 2 is the winner!')

print(f"\nThanks for playing Tic-Tac-Toe!\n")
