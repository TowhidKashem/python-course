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

# default arguments can also be passed at the time of invoking the function for better readability, it must match the variable name used in the function definition
# doing it this way also means arguments can be in any order
greet(name="Joe")  # Hello Joe!


# keyword arguments lets you switch up the order of the arguments, works like using an object as the param
def say_name_and_age(name, age):
    print("Hello " + name + ", you are " + age + " years old!")


say_name_and_age(age=33, name="Joe")


# if you don't know the number of arguments that will be passed, use *args, same as `arguments` keyword in js
# this will allow all arguments to be accessible as a list
# kids = ['Emil', 'Tobias']
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias")


# same as above but for an unknown number of keyword arguments
# kid = { first_name: "Towhid", last_name: "Kashem" }
def my_function(**kid):
    print("His last name is " + kid["last_name"])


my_function(first_name="Towhid", last_name="Kashem")


# to avoid errors when writing a function as a temp placeholder, using "pass" is equivilent to just "return"ing nothing
def do_something():
    pass


# lambda functions are one liners, they can take any number of args but can only have 1 expression
# same as "const add_ten = (x) => x + 10"
def add_ten(x): return x + 10
