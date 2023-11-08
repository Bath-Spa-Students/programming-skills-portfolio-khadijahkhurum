# Initializing the lists
sandwich_orders = ['tuna', 'ham', 'egg salad', 'veggie']
finished_sandwiches = []

# Looping through the orders and printing a message for each
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

# Printing the list of finished sandwiches
print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)