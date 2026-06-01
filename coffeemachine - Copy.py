from pprint import pprint

#adding resources and manage money
class machine:
    def __init__(self,resources):
        self.water = resources["water"]
        self.milk = resources["milk"]
        self.coffee = resources["coffee"]
        self.coins = resources["coins"]


    # check if ingredients are enough to make coffee
    def checkIngredients(self,ingredients):
        if(self.water >= ingredients["water"] and self.milk >= ingredients["milk"] and self.coffee >= ingredients["coffee"]):
            self.deductIngredients(ingredients)
            return True
    
    #deduct amount of ingredients
    def deductIngredients(self,ingredients):
        self.water -= ingredients["water"]
        self.milk -= ingredients["milk"]
        self.coffee -= ingredients["coffee"]
    
    # get details of resources and money
    def getDetails(self):
        print(f"\nResources:\nWater: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}gm")
        print(f"\n\nMoney Collected: ${round(self.coins,2)}")

    #refill the machine
    def refill(self,resources):
        self.milk = resources["milk"]
        self.water = resources["water"]
        self.coffee = resources["coffee"]
        print("\nCoffee machine is refilled")

    #count money collected
    def countCoins(self,money):
        self.coins += money

    def getIngredients(self,ingredients):
        pprint(ingredients["coffee"])

    def getAmountofIngredients(self):
        print(f"\nMilk: {self.milk}\nWater: {self.water}\nCoffee: {self.coffee}")
    

            