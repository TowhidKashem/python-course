# sets don't guarantee insertion order and contain only unique values
# unlike tuples sets are mutable, values can be added or removed at any time

fruits = {"apple", "banana", "cherry"}

fruits.add('orange')  # add an element to the set

# add items from a list to the set
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# remove an element from the set, if elem doesn't exist throws error
fruits.remove('banana')

# remove an element from the set, if elem doesn't exist fails silently
fruits.discard('banana')
