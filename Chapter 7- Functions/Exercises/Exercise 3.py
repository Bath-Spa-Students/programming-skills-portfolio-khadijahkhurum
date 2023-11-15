def make_shirt(size, message):
    print(f"Your {size} shirt says '{message}'.")

# Call the function once using positional arguments to make a shirt.
make_shirt('large', 'Hello World')

# Call the function a second time using keyword arguments.
make_shirt(size='medium', message='Python Programming')