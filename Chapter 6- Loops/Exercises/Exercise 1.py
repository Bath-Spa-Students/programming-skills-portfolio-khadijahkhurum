toppings = []

while True:
    topping = input("Enter a pizza topping, or 'quit' to stop: ")
    
    if topping.lower() == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"You'll add {topping} to your pizza.")

print("\nHere are your final toppings:")
for topping in toppings:
    print(topping)