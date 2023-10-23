#Start with the list you used in Exercise 1, but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.


# Create a list of your friends' names
names = ["John", "Reighn", "LLoyd", "Ifrah", "Francis"]

# Print personalized messages to each person
for name in names:
    message = f"Hello, {name}! I hope you're having a great day."
    print(message)
