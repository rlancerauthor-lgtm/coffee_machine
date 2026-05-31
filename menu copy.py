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
       while True:
        
         if tryNum == 0:
           print(f"\nThe cost of {coffee} is ${cost}\nPlease insert coins")
           coinsCollected += self.showCoinMenu()
         else:
          while True:
             print(f"\nThe cost of {coffee} is ${cost}\nStill ${round((cost-coinsCollected),2)} remaining")
             cnt = input("\nPlease press 'M' for inserting more coins or any other key to quit: ").lower()
             if cnt == "m":
                coinsCollected += self.showCoinMenu()
                tryNum = 1
                print(f"{coinsCollected}")
                if cost > coinsCollected:
                 continue
                else:
                 print(f"\nPlease take the change of ${round((coinsCollected - cost),2)}")
                 print(f"\nPlease enjoy your {coffee} ☕")
                 return
             else:
                 print(f"\nThank you for visiting. Please collect ${round(coinsCollected,2)}")
                 return
                 
         
         
       
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
   
          
       
       
    
       

