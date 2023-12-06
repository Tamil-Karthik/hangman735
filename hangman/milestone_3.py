import random

#TODO - Define a method to randomly choose a word from a list of words
word_list = ['apple','orange','banana','mango','grapes'] 
word = random.choice(word_list)
print(word)
#def choice(word_list):
    #word = random.choice(word_list)
    #print(word)
    #return word

def check_guess(guess):
    guess = guess.lower()
    #word = choice(word_list)
    if (guess in word):
         print(f"Good guess! {guess} is in the word.")
    else:
         print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while(True):
        guess = input("Guess a letter: ")
        if (len(guess) == 1 and guess.isalpha()): #TODO - Check if the user input is an alphabet    
          break
        else:
          print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
    