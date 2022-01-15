# assign the same value to multiple variables
a = b = c = 'wow'


def myfunc():
    global x  # x is now a variable defined and available in the global scope
    x = "fantastic"


###

name = 'Julia'


def myfunc():
    name = "TK"  # this is a local variable, the global one is unchanged


myfunc()
print(name)  # name is still "Julia"

# this works UNLIKE js:

# let name = 'Julia'
# function changeName() {
#   name = 'TK'
# }
# changeName();
# console.log(name); // "TK"


def myfunc():
    global name  # this will cause name to be changed in the global scope to "TK"
    name = "TK"


###

# same as `typeof`
type('abc')  # str
type(10)  # int
type(1.5)  # float
type([1, 2, 3])  # list
type(("apple", "banana", "cherry"))  # tuple
type({"name": "John", "age": 36})  # dict
type(True)  # bool
