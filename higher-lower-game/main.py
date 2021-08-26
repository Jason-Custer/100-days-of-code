# Higher Lower Game

import random
from replit import clear
from game_data import data
from art import logo
from art import vs


# Variables
score = 0
random_B = random.choice(data)

print(logo)

game_over = False

while game_over == False:

    # Generate two random items from the dictionary:

    random_A = random_B
    random_B = random.choice(data)

    while random_A == random_B:
        random_B = random.choice(data)

    # Function to present a higher-lower pair:
    def generate_comparison(random):
        '''Returns printable random information.'''
        name = random["name"]
        description = random["description"]
        country = random["country"]
        return(f"{name}, a {description} from {country}.")

    print(f"Compare A: {generate_comparison(random_A)}")
    print(vs)
    print(f"Against B: {generate_comparison(random_B)}")

    # Input answer
    answer = (input("Who has more followers? Type 'A' or 'B':\n")).lower()

    # Check the answer:

    follower_count_A = random_A["follower_count"]
    follower_count_B = random_B["follower_count"]

    if answer == "a":
        if follower_count_A > follower_count_B:
            clear()
            score += 1
            print(f"You're right! Current score: {score}")
            print(logo)
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
    elif answer == "b":
        if follower_count_B > follower_count_A:
            clear()
            score += 1
            print(f"You're right! Current score: {score}")
            print(logo)
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
    else:
        print("Invalid entry.")
