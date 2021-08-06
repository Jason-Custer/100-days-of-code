# Tip Calculator

print("Welcome to the tip calculator!")

bill = float(input("How much was the bill? $"))
tip = float(input("What percentage tip do you want to give? "))
people = int(input("How many people are splitting the bill? "))
total = (bill * (1 + (tip / 100))) / people
total_rounded = "{:.2f}".format(total)

print(f"Each person should pay ${total_rounded}")
