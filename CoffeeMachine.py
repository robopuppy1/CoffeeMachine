from coffee_maker import CoffeeMaker
from menu import MenuItem, Menu
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while True:

  choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

  if choice == 'off':
    break
  elif choice == 'report':
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
