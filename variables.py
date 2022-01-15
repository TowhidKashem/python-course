# assign the same value to multiple variables
a = b = c = 'wow'


def myfunc():
    global x  # x is now a variable in the global scope
    x = "fantastic"


# same as `typeof`
type('abc')  # str
type(10)  # int
type(1.5)  # float
type([1, 2, 3])  # list
type(("apple", "banana", "cherry"))  # tuple
type({"name": "John", "age": 36})  # dict
type(True)  # bool
