import random

class Hangman:
    def __init__ (self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = [None,None,None,None,None]
        self.num_letters = 0
        self.list_of_guesses = []

    def check_guess(self, guess):
        self.guess = guess.lower()  
        #index = self.word.find(self.guess)  
        if (self.guess in self.word):
            print(f"Good guess! {guess} is in the word.")
            for letter in range(len(self.word)):
                if (self.word[letter] == guess):
                    self.word_guessed[letter] = guess
            self.num_letters -= 1      
        else:
            self.num_lives -= 1  
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while(True):
            guess = input("Guess a letter: ")
            if (len(guess) != 1 and guess.isalpha() != True): #TODO - Check if the user input is an alphabet    
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif(guess in self.list_of_guesses):
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
    
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while(True):
        if game.num_lives == 0:
            print("\'You lost!\'")
        if game.num_letters > 0:
            game.ask_for_input()
        if (game.num_lives != 0 and game.num_letters <= 0):
            print("\'Congratulations. You won the game!\'")
           

word_list =  ['apple','orange','banana','mango','grapes'] 
play_game(word_list)
