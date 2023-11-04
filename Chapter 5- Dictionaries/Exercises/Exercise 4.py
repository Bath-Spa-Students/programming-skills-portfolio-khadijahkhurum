# Create a dictionary of rivers and the countries they run through
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

for river, country in rivers.items():
    print(f'The {river} runs through {country}.')


print("\nList of rivers:")
for river in rivers.keys():
    print(river)

# Use a loop to print the name of each country
print("\nList of countries:")
for country in rivers.values():
    print(country)
