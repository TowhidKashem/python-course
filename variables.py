# assign the same value to multiple variables
a = b = c = 'wow'


def my_func():
    global x  # x is now a variable defined and available in the global scope
    x = "fantastic"


###

name = 'Julia'


def my_func():
    name = "TK"  # this is a local variable, the global one is unchanged


my_func()
print(name)  # name is still "Julia"

# this works UNLIKE js:

# let name = 'Julia'
# function changeName() {
#   name = 'TK'
# }
# changeName();
# console.log(name); // "TK"


def my_func():
    global name  # this will cause name to be changed in the global scope to "TK"
    name = "TK"


###
