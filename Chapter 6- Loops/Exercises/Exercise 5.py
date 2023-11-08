# Initializing the lists
sandwich_orders = ['tuna', 'ham', 'egg salad', 'veggie', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

# Checking if there are at least three pastrami sandwiches in the list
pastrami_count = sandwich_orders.count('pastrami')

if pastrami_count < 3:
    print("The deli has run out of pastrami.")

    # Removing all occurrences of 'pastrami' from sandwich_orders
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

# Looping through the orders and printing a message for each
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

# Printing the list of finished sandwiches
print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)