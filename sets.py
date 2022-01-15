fruits = {"apple", "banana", "cherry"}

"apple" in fruits  # True

fruits.add('orange')  # add an element to the set

# add multiple elements to the set
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# remove an element from the set, if elem doesn't exist throw error
fruits.remove('banana')

# remove an element from the set, if elem doesn't exist fail silently
fruits.discard('banana')
