


list = ["Zuraira Faisal", "Muhammad Anwar", "Khursheed Anwar, Amray Abbas"]

print("Due to a delay, I can only invite two people for dinner.")

while len(list) > 2:
    RG = list.pop()
    print(f"Sorry, {RG}, I can't invite you to dinner this time.")

for person in list:
    print(f"Dear {person},\nYou are still invited to join me for a dinner gathering.\nPlease let me know if you can attend.\nSincerely, Khadijah.")

del list[0]  
del list[0]  

print("Updated list of guests:", list)
