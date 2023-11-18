
list = ["Zuraira Faisal", "Muhammad Anwar", "Khursheed Anwar"]

unavail = "Khursheed Anwar"
print(f"Unfortunately, {unavail} can't make it to the dinner.")

# Replace the guest who can't make it with a new person
newG = "John Maverick"
list.remove(unavail)
list.append(newG)

for person in list:
     print(f"Dear {person},\nYou are invited to join me for a dinner gathering. Your contributions to my life and the person I have become are have made me beyond thankful. To have you as my guest for dinner would be an honour. \nPlease let me know if you can attend.\nSincerely, Khadijah.")