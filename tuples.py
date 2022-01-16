# tuples are immutable, once made can't be changed, are ordered like regular lists and can contain duplicates

fruits = ("apple", "banana", "cherry")

# parenthesis are optional unless the tuple has only 1 value
fruits = "apple", "banana", "cherry"

fruits[1] = "banana"

"apple" in fruits  # True
