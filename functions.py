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
