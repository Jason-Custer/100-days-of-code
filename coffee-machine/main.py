# Variables:
from data import MENU
from data import resources

cash_inserted = 0
money = 0

machine_off = False

while not machine_off:
    def check_resources(coffee):
        if (resources["water"] - MENU[coffee]["ingredients"]["water"]) < 0:
            print("Sorry, there is not enough water.")
        if (resources["milk"] - MENU[coffee]["ingredients"]["milk"]) < 0:
            print("Sorry, there is not enough milk.")
        if (resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]) < 0:
            print("Sorry, there is not enough coffee.")
        else:
            pass

    def complete_order(coins, coffee):
        change = round((coins - float(MENU[coffee]['cost'])), 2)
        print(f"Here is ${change} in change.")
        print("Here is your " + str(coffee) + ". Enjoy!")
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]


    # TODO 1. Ask user what they want ("espresso/latte/cappuccino").

    order = input("What would you like? (espresso/latte/cappuccino)\n").lower()

    # TODO 2. Turn off coffee machine with "off" prompt.

    if order == "off":
        print("Goodbye!")
        machine_off = True

    # TODO 3. Print report with "report" prompt.

    elif order == "report":
        print(f'''
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        Money: ${money}
        ''')

    # TODO 4. Check if there are sufficient resources.
    else:
        if order == "espresso":
            check_resources("espresso")

        elif order == "latte":
            check_resources("latte")

        elif order == "cappuccino":
            check_resources("cappuccino")

        else:
            order = input("Invalid entry. Try again: What would you like? (espresso/latte/cappuccino)\n")

    # TODO 5. Process the coins entered.
        print("Please insert coins: ")

        quarters = int(input("How many quarters? "))
        cash_inserted += (quarters * 0.25)

        dimes = int(input("How many dimes? "))
        cash_inserted += (dimes * 0.10)

        nickels = int(input("How many nickels? "))
        cash_inserted += (nickels * 0.05)

        pennies = int(input("How many pennies? "))
        cash_inserted += (pennies * 0.01)

        # TODO 6. Check if the transaction is successful.
        # TODO 7. Make the coffee.

        if cash_inserted >= MENU[order]["cost"]:
            complete_order(cash_inserted, order)
            money += MENU[order]["cost"]
        else:
            cash_inserted = 0
            print("Sorry, that's not enough money. Money refunded.")



