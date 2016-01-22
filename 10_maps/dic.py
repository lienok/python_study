# create a mapping of country to abbreviation
countries = {
    'Slovakia': 'SK',
    'Czech Republik': 'CZ',
    'Austria': 'AT',
    'Poland': 'PL',
    'Germany': 'DE'
}

# create a basic set of countries and some cities in them
cities = {
    'SK': 'Bratislava',
    'CZ': 'Prague',
    'DE': 'Berlin'
}

# add some more cities
cities['AT'] = 'Vienna'
cities['PL'] = 'Warsaw'

# print out some cities
print '-' * 10
print "SK Country has: ", cities['SK']
print "PL Country has: ", cities['PL']

# print some countries
print '-' * 10
print "Slovakia's abbreviation is: ", countries['Slovakia']
print "Czech Republik's abbreviation is: ", countries['Czech Republik']

# do it by using the country then cities dict
print '-' * 10
print "Slovakia has: ", cities[countries['Slovakia']]
print "Czech Republik has: ", cities[countries['Czech Republik']]

# print every country abbreviation
print '-' * 10
for state, abbrev in countries.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in country
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
	
# now do both at the same time
print '-' * 10
for state, abbrev in countries.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
	
print '-' * 10
# safely get a abbreviation by state that might not be there
state = countries.get('France')

if not state:
    print "Sorry, no France."  
	
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')  #For key 'TX', returns value or default message if key not in dictionary
print "The city for the state 'TX' is: %s" % city

