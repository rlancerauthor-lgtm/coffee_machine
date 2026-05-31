from pprint import pprint

class menu:
    def __init__(self,menudict):
      self.menudict = menudict
     #self.coinsCollected = 0

    def displayMenu(self):
       while True:
          coffeeDrink = input("\nWhat would you like to order?\nCappuccino, Latte or Espresso?\n").lower()
          if coffeeDrink not in ["cappuccino","latte","espresso"]:
             print("\nPlease enter a coffee drink from menu")
             continue
          else:
             break
          
       return coffeeDrink
    
    def getIngredients(self,coffee):
       return self.menudict[coffee]["ingredients"]
    
     # get cost of coffee
    def getCost(self,coffee):
        return self.menudict[coffee]["price"]
    
    # menu for collecting coins
    def collectCoins(self,coffee):
       cost = self.getCost(coffee)
       coinsCollected = 0
       tryNum = 0
      
       print(f"\nThe cost of {coffee} is ${cost}\nPlease insert coins")
       coinsCollected += self.showCoinMenu()
        
       if cost > coinsCollected:
         print(f"\nSorry, the amount is insufficient\nPlease take back change of ${round((coinsCollected),2)}")
         coinsCollected = 0
       else:
         print(f"\nPlease take the change of ${round((coinsCollected - cost),2)}")
         print(f"\nPlease enjoy your {coffee.capitalize()} ☕")
       return coinsCollected
           
                 
         
         
       
    def showCoinMenu(self):
       while True:
          try:
            quarters = int(input("\nHow many quarters? "))
            break
          except:
            print("\nPlease insert a number")

       while True:
          try:
           dimes = int(input("\nHow many dimes? "))
           break
          except:
            print("\nPlease insert a number")

       while True:
          try:
           nickles = int(input("\nHow many nickles? "))
           break
          except:
            print("\nPlease insert a number")

       while True:
          try:
           pennies = int(input("\nHow many pennies? "))
           break
          except:
            print("\nPlease insert a number")

       return self.countCoins(quarters,dimes,nickles,pennies)

    def countCoins(self,quarters,dimes,nickles,pennies):
       
       return (quarters * 0.25)+(dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
   
          
       
       
    
       

