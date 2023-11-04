# Create a list of dictionaries representing different pets
pets = [
    {
        'kind': 'Dog',
        'owner': 'Lydia',
    },
    {
        'kind': 'Mouse',
        'owner': 'Lionel',
    },
    {
        'kind': 'Snake',
        'owner': 'Drake',
    },
    {
        'kind': 'Bird',
        'owner': 'Jeena',
    },
]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Kind of animal: {pet['kind']}")
    print(f"Owner's name: {pet['owner']}")
    print()  # Empty line to separate each pet's information
