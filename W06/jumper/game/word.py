import random


class Word:

    def __init__(self):
        self._word_list = ["fox", "cat", "happy", "drama",
                           "cartoons", "television", "biscuits", "wifi", "laptop"]
        # self._word_list = ["cat"] # Used this line for testing so I had the same word every time.
        self._random_word = random.choice(self._word_list)
        self._guess_state = []

        for x in self._random_word:
            self._guess_state.append("_")

        #print(*self._guess_state)  # Used in class test. In Python 3 we can use the * as an unpacking operator and print the list separated by spaces.

    def print_clue(self):
        print(*self._guess_state) # In Python 3 we can use the * as an unpacking operator and print the list separated by spaces. Probably better to use the 'join()' function like so print(" ".join(self._guess_state)) adding a space in the "" to space the letters out.
        print() # adds blank line after the clue for spacing.
        #for i in self._guess_state: # loops through each letter in self._guess_state and then prints it.
        #    print(i, end="") # Here we use the 'end=""' method to print the list on the same line. If you want a space between letters, just add a space in the string for end like this (end=" ")
        return self._guess_state # Returns the current self._guess_state used in our _do_updates() function.

    
    def check_guess_matches(self, guessed_character):
        if guessed_character in self._random_word:
            i = 0
            for x in self._random_word:
                if x == guessed_character:
                    self._guess_state[i] = x
                i += 1

            #print(*self._guess_state)  # Used in class test. In Python 3 we can use the * as an unpacking operator and print the list separated by spaces.
            #print("".join(self._guess_state))  # Used in class test. Use this line to join the word without spaces.
            return True # Returns 'True'
        else:
            return False # Returns 'False'

    def word_match_complete(self):
        if "".join(self._guess_state) == self._random_word:
            return True
        else:
            return False


# What follows below is for testing the class
#word = Word()
#word.print_clue()
#word.check_guess_matches('a')