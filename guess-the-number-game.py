#Number Guessing Game Objectives:

import random

# Variables:
attempts = 0
guess = 0

# Code asking to select difficulty (easy = 10 guesses, hard = 5 guesses):

print("Welcome to the Guess the Number Game!\n I am thinking of a number between 1 and 100.")
difficulty = input("Select your difficulty - type 'easy' or 'hard': ")
difficulty = difficulty.lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("You entered an invalid choice:")
    difficulty = input("Type either 'easy' or 'hard': ")

# Code for inputing guess:

guess = int(input("Guess a number between 1 and 100:\n"))

# Code for creating a random number between 1-100:

number = random.randint(1,100)

# Code to compare guess to actual number:

game_over = False

while game_over == False:
    if guess == number:
        print(f"You guessed correctly, the number is {number}.")
        game_over = True
    else:
        if attempts <= 1:
            game_over = True
            print(f"You ran out of attempts. You lose.\n The number was {number}")
        else:
            if guess < number:
                print("Your guess is too low.")
                print(f"You have {attempts-1} attempts remaining.")
                attempts -= 1
                guess = int(input("Guess again:\n"))
            elif guess > number:
                print("Your guess is too high.")
                print(f"You have {attempts-1} attempts remaining.")
                attempts -= 1
                guess = int(input("Guess again:\n"))


