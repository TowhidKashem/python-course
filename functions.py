# def replaces function keyword, : replaces {}
# no semi colons, use indentation (4 spaces only)
def say_hello():
    print("Hello World!")


say_hello()


# arguments and return statements work the same
def sum(a, b):
    return a + b


sum(1, 2)  # 3


# default arguments work the same
def greet(name="Stranger"):
    print("Hello " + name + "!")


greet()  # Hello Stranger!
greet("Joe")  # Hello Joe!


# keyword arguments lets you switch up the order of the arguments, works like using an object as the param
def sayNameAndAge(name, age):
    print("Hello " + name + ", you are " + age + " years old!")


sayNameAndAge(age=33, name="Joe")


# if you don't know the number of arguments that will be passed, use *args, same as `arguments` keyword in js
# this can then be used as a list
def my_function(*kids):
    print("The youngest child is " + kids[2])


# same as above but for an unknown number of keyword arguments
def my_function(**kid):
    print("His last name is " + kid["lname"])


# to avoid errors when writing a function as a temp placeholder
# using "pass" is equivilent to just "return" nothing
def do_something():
    pass
