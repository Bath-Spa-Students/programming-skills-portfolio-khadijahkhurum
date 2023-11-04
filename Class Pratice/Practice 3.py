
age = int(input("Enter your age: "))

if age < 6:
    print("You are an infant.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
elif age > 65:
    print("You are a senior citizen.")
else:
    print("Invalid age entered.")
