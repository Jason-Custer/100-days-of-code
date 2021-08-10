# Rock Paper Scissors Game
import random

print("Welcome to Rock, Paper, Scissors!")

# Code to get the player input:

player_choice = input("Enter your selection ('R' for Rock, 'P' for Paper, and 'S' for Scissors:\n")

player_choice = player_choice.lower()
player_move = 3


if player_choice == "r":
  player_move = 0
elif player_choice == "p":
  player_move = 1
elif player_choice == "s":
  player_move = 2
else:
  print("You entered an invalid choice - try again.")

# Code to randomize the computer choice:

computer_move = random.randint(0, 2)

# Code that displays the two moves:

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if player_move == 0:
  print(f"You play:\n{rock}")
if player_move == 1:
  print(f"You play:\n{paper}")
if player_move == 2:
  print(f"You play:\n{scissors}")

if computer_move == 0:
  print(f"Computer plays:\n{rock}")
if computer_move == 1:
  print(f"Computer plays:\n{paper}")
if computer_move == 2:
  print(f"Computer plays:\n{scissors}")

# Code to compare the two choices and return the winner:

if player_move == computer_move:
  print("It's a tie! Play again.")

if player_move == 0 and computer_move == 1:
  print("Paper beats Rock - you lose!")
if player_move == 1 and computer_move == 2:
  print("Scissors beats Paper - you lose!")
if player_move == 2 and computer_move == 0:
  print("Rock beats Scissors - you lose!")

if player_move == 1 and computer_move == 0:
  print("Paper beats Rock - you win!")
if player_move == 2 and computer_move == 1:
  print("Scissors beats Paper - you win!")
if player_move == 0 and computer_move == 2:
  print("Rock beats Scissors - you win!")

