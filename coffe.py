water = 300
milk = 200
coffee = 100
money = 0
transaction = True


def coins():
    global transaction
    global money
    print("Please insert you coin.")
    coin1 = int(input("How many quarters?: "))
    coin2 = int(input("How many dimes?: "))
    coin3 = int(input("How many nickles?: "))
    coin4 = int(input("How many pennies?: "))
    money1 = float(coin1*0.25+0.1*coin2+ 0.05*coin3+0.01*coin4)
    money = money1
    if money1 > 2.5:
        change = money1-2.5
        print(f"Here is your {user_demand} ☕. Enjoy!")
        print(f"Here is Your ${change} in change.")
        transaction = True

    elif money1 > 1.5:
        change = money1 - 1.5
        print(f"Here is your {user_demand} ☕. Enjoy!")
        print(f"Here is Your ${change} in change.")
        transaction = True

    elif money1 > 3:
        change = money1-3
        print(f"Here is your {user_demand} ☕. Enjoy!")
        print(f"Here is Your ${change} in change.")
        transaction = True

    elif money1 == 2.5 or money1 == 1.5 or money1 == 3:
        print(f"Here is your {user_demand}.Enjoy!")
        transaction=True
    elif money1 < 2.5 or money1 < 1.5 or money1 < 3:
        print("Sorry that,s not enough money .Money refunded")
        transaction = False


is_on = True
while is_on:
  user_demand = input("What would you like (espresso/cappuccino/latte) : ")
  if user_demand == "off":
     is_on=False
  elif user_demand == "latte":
    if milk < 150:
     print("Sorry there is not enough milk")
    elif water < 200:
        print("Sorry there is not enough water")
    elif coffee < 24:
        print("Sorry there is not enough coffee")
    else:
     coins()
     if transaction == True:
      milk = milk - 150
      water = water-200
      coffee = coffee-24
  elif user_demand == "espresso":
    if water< 50:
        print("Sorry there is not enough water")
    elif coffee< 18:
        print("Sorry there is not enough coffee")
    else:
     coins()
     if transaction == True:
      water = water-50
      coffee = coffee-18
  elif user_demand == "cappuccino":
   if milk < 100:
     print("Sorry there is not enough milk")
   elif water < 250:
        print("Sorry there is not enough water")
   elif coffee < 24:
        print("Sorry there is not enough coffee")
   else:
     coins()
     if transaction == True:
      milk = milk - 100
      water = water-250
      coffee = coffee-24
  elif user_demand == "report":
    print(f"Water : {water}ml")
    print(f"Milk : {milk}ml")
    print(f"Coffee : {coffee}ml")
    print(f"Money : ${money}")
