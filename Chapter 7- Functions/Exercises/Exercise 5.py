def describe_city(city, country='USA'):
    print(f'{city} is in {country}.')

# Call the function for three different cities
describe_city('New York') # The default country is USA
describe_city('London', 'England') # This city is not in the default country
describe_city('Tokyo', 'Japan') # This city is not in the default country
