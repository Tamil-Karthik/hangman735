import random

#TODO - Define a method to randomly choose a word from a list of words
def choice(word_list):
    word = random.choice(word_list)
    print(word)

word_list = ['apple','orange','banana','mango','grapes'] 
choice(word_list)

guess = input("Enter a letter of your choice: ") #TODO - Get a letter from user
if (len(guess) == 1 and guess.isalpha()): #TODO - Check if the user input is an alphabet
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")