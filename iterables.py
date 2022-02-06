# iterables can be looped and share many common properties and functions
# in python strings, lists, dictionaries, sets and tuples are all iterables

foods = "apple, broccoli, chicken"
foods = ['apple', 'broccoli', 'chicken']
foods = ('apple', 'broccoli', 'chicken')
foods = {'apple', 'broccoli', 'chicken'}
foods = {'apple': 1, 'broccoli': 2, 'chicken': 3}


# get number of items inside (list, tuple, set)
# get number of key/value pairs inside (dictionary)
# get number of characters inside (string)
print(len(foods))


# loop over all values (list, dictionary, tuple, set)
# loop over each character (string)
for food in foods:
    print(food)

# loop over all values (list, dictionary, tuple, set)
# loop over each character (string)
#   "food" is is a tuple (index, value), can use this if index is needed
#   can unpack for easy access: for (index, value) in enumerate(foods):
for food in enumerate(foods):
    print(food)  # (0, 'apple')


# grab value by index (list, tuple)
# grab character by index (string)
print(foods[1])
print(foods[-1])  # negative indices grab from the end

# grab values by index range (list, tuple)
# grab characters by index range (string)
print(foods[0:2])


# change value by index (list)
# add value by key (dictionary)
foods[1] = 'eggs'
print(foods)


# destructing aka unpacking values (list, tuple)
# also works on sets and dictionaries but no real use case there since it only extracts the key names not the values
# for destructing those use `itemgetter()` from the standard library
fruit, veggie, meat = foods
print(meat)


# check if value exists (string, list, tuple, set)
# check if key exists (dictionary)
if "apple" in foods:
    print("apple is found in foods")

if "cucumber" not in foods:
    print("cucumber not found in foods")


# join all values seperated by a delimeter into a string (list, dictionary, tuple, set)
# joins all characters into a string (string)
print('-'.join(foods))  # apple-broccoli-chicken

# split a string based on provided delimeter
foods.split('-')  # ['apple', 'broccoli', 'chicken']
