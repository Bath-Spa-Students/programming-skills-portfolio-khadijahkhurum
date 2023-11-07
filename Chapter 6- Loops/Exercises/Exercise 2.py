while True:
    try:
        age = int(input("Enter your age: "))
        if age < 3:
            print("Your ticket is free!")
        elif 3 <= age <= 12:
            print("The cost of your movie ticket is AED 10.")
        elif age > 12:
            print("The cost of your movie ticket is AED 15.")
        else:
            print("Invalid age entered. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")