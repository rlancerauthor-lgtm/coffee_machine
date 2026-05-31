from menu import menu
from coffeemachine import machine

#menu dictionary
menu_list = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 20,
        },
        "price": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 150,
            "milk": 200,
            "coffee": 25,
        },
        "price": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 25,
        },
        "price": 3.0,
    }
}

# ingredients dictionary
resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 100,
    "coins": 0
}

# initialize classes
coffee_menu = menu(menu_list)
coffeemachine = machine(resources)

#variable for machine on/off
machineStatus = "off"

#function for checking if machine is on or off
def check_machine_status():
    global machineStatus
    if(machineStatus == "off"):
        while True:
          task = input("\nWhat you want to do?\nPress 'C' to check resources & money collected\nPress 'R' for refill the machine\nPress 'O' for turning the machine on: ").lower()
          if task not in ["c","r","o"]:
            print("\nPlease enter either 'C','R','O'")
            continue
          else:
             
             match(task):
                case 'c':
                    coffeemachine.getDetails()
                case 'r':
                    coffeemachine.refill(resources)
                case 'o':
                    machineStatus = "on"
                    check_machine_status()
    else:
        while True:
            drink = coffee_menu.displayMenu()
            if coffeemachine.checkIngredients(coffee_menu.getIngredients(drink)):
               totalCoins =  coffee_menu.collectCoins(drink)
               coffeemachine.countCoins(totalCoins)
              
            else:
                print("\nSorry, there aren't enough resources for coffee")
                machineStatus = "off"
                check_machine_status()
                     
               
          
check_machine_status()

