from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Variables:

drink_menu = Menu()
coffee_maker = CoffeeMaker()
cashier = MoneyMachine()

machine_on = True

# TODO 1. Ask user what they want ("espresso/latte/cappuccino").

while machine_on:
    order = str(input(f"What would you like to drink? ('{drink_menu.get_items()}'):\n")).lower()

# TODO 2. Turn off coffee machine with "off" prompt.

    if order == "off":
        machine_on = False

# TODO 3. Print report with "report" prompt.

    elif order == "report":
        coffee_maker.report()
        cashier.report()

# TODO 4. Check if there are sufficient resources.

    else:
        drink = drink_menu.find_drink(order)

        if coffee_maker.is_resource_sufficient(drink):

            # TODO 5. Process the coins entered.
            # TODO 6. Check if the transaction is successful.

            cashier.make_payment(drink.cost)

            # TODO 7. Make the coffee.2

            coffee_maker.make_coffee(drink)
