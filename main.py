import random
from words import words

word = random.choice(words)
guesses = []
done = False
numberOfGuesses = 7
#run a loop for the user to guess the word
while not done:
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
        else:
            print("_",end=" ")
    print("\n")
    guess = input("please type a letter to guess: ")
    #add the user input to the empty guesses list
    guesses.append(guess)
    #subtract the number of guesses from the user
    if guess not in word:
        numberOfGuesses -= 1
        if numberOfGuesses == 0:
            break

    done = True
    for letter in word:
        if letter not in guesses:
            done = False
#jump out of the while loop and print you win and you lost
if done:
    print(f"wow you guessed it the word is {word}")
else:
    print(f"sorry you're out of guesses the word is {word}")