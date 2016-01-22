stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2} #define dictionary with 3 items
print stuff
assert stuff['name']=="Zed","Attention! expected Zed"
assert stuff['age'] == 39, "Attention! Expected 39"
assert stuff['height'] == 74, "Attention! Expected 74"

stuff['city'] = "San Francisco" #add key "city" to the dictionary, with a value "San Francisco"
assert stuff['city'] == "San Francisco", "Attention! Expected San Francisco"

stuff[1] = "Wow"  #we can add number as a key
stuff[2] = "Neato"

assert stuff[1] == "Wow", 'Attention! Expected "Wow"'
assert stuff[2] == "Neato", 'Attention! Expected "Neato"'
print stuff

del stuff['city']  #delete from stuf item with the key "city"
del stuff[1]
del stuff[2]