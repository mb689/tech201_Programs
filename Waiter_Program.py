print("---------------------------------------------")
print("-------------------Starters------------------")
print("1) Salad ")
print("2) Deviled Eggs ")
print("3) Soup ")
print("4) Stuffed Mushrooms ")
print("-------------------Main Menu-----------------")
print("1) Grilled chicken breast ")
print("2) Beef stir-fry ")
print("3) Pasta dish ")
print("4) Vegetable curry ")
print("-------------------Desserts------------------")
print("1) Cheesecake ")
print("2) Strawberry Shortcake ")
print("3) Chocolate Brownies ")
print("")
print("Please place your order!!!!")
customer_Order = []

starter = input("What starter would you like? ")
customer_Order.append(starter)
main_menu = input("What main would you like? ")
customer_Order.append(main_menu)
desserts = input("What dessert would you like? ")
customer_Order.append(desserts)

print("")
print("-------------------Your order is-------------------")
print(f"Starter: {customer_Order[0]}, Main: {customer_Order[1]}, Dessert: {customer_Order[2]}")
print("---------------------------------------------------")