def make_shirt(size='large', message='I love Python'):
    print(f"Your {size} shirt says '{message}'.")

# Call the function with the default size and message
make_shirt()

# Call the function with the default size and a custom message
make_shirt(message='Hello World')

# Call the function with a custom size and the default message
make_shirt(size='medium')

# Call the function with a custom size and message
make_shirt(size='small', message='Python Programming')