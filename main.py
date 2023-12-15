from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menu = Menu()
#
# choice = input(f"What would you like? ({menu.get_items()})".lower())
# print(choice)
# print(menu.find_drink(choice))
#
# #print(menu.menu)
# menu = MenuItem(choice, "water", "milk", "coffee", "cost")
# print(menu)
# print(menu.cost)

######
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#dummy variable to stop while loop when off is entered
is_on = True

while is_on == True:
    choice = input(f"What would you like? ({menu.get_items()})".lower())
    #print(choice)
    menu_item = MenuItem(choice, "water", "milk", "coffee", "cost")
    if choice == "off": # stop loop and turn off
        is_on = False
    elif choice == "report": # print report
        coffee_maker.report()
        money_machine.report()
    else: #check resources
        drink = menu.find_drink(choice)
        #print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            #process coins and check if successful
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            # else:
            #     is_on = False



#print(menu.find_drink(choice))
# drink = coffee_maker.is_resource_sufficient(menu_item)
# coffee_maker.is_resource_sufficient(choice)


#if choice == "off"
