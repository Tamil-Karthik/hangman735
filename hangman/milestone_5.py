import random

class Hangman:

    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''

    def __init__ (self, word_list,num_lives):

        '''
        Initialize the attributes
        '''

        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)        
        self.word_guessed = ['_','_','_','_','_']
        self.num_letters = 5
        self.list_letters = []    

    def ask_letter(self): 

        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''

        while(True):
            if(self.num_lives == 0 and self.num_letters <= 0):
                break
            else:
                letter = input("Guess a letter: ")
                if (len(letter) != 1 or letter.isalpha() != True): #TODO - Check if the user input is an alphabet    
                    print("Invalid letter. Please, enter a single alphabetical character.")
                    break
                elif(letter in self.list_letters):
                    print("You already tried that letter!")
                    break
                else:
                    self.list_letters.append(letter)
                    self.check_letter(letter)
                    break

    def check_letter(self, letter):

        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        
        letter = letter.lower()          
        if (letter in self.word):
            print(f"Good guess! {letter} is in the word.")
            for alphabet in range(len(self.word)):
                if (self.word[alphabet] == letter):
                    self.word_guessed[alphabet] = letter               
                    self.num_letters = self.num_letters - 1                                          
        else:
            self.num_lives = self.num_lives - 1          
            print(f"Sorry, {letter} is not in the word.")            
            print(f"You have {self.num_lives} lives left.")
        return
    
def play_game(word_list):

    '''
    Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    If the user guesses the word, print "Congratulations! You won!"
    If the user runs out of lives, print "You lost! The word was {word}"

    Parameters:
        ----------
        word_list: list
            The list of words to be randomly chosen
    '''

    num_lives = 5
    game = Hangman(word_list,num_lives)    
    while(True):
        if game.num_lives == 0:
            print(f"\'You lost!\' The word was {game.word}")        
            break    
        elif game.num_letters > 0:            
            game.ask_letter()                        
        elif (game.num_lives != 0 or game.num_letters <= 0):
            print("\'Congratulations. You won the game!\'")
            print(f"yes, the word is {game.word}")
            break                      

word_list =  ['melon','berry','peach','mango','grape'] 
play_game(word_list)
