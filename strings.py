# convert any data type to a string, similar to toString() and JSON.stringify(obj)
str({'a': 1, 'b': 2})  # "{'a': 1, 'b': 2}"

# concatenate strings, same as js
name = 'John' + ' ' + 'Doe'

# repeat a string x times, same as 'hello'.repeat(10)
sayHelloTenTimes = 'Hello' * 10

# span mutiple lines with triple quotes, same as using backticks
# `greeting` will have \n for the line breaks in it
greeting = """hello
world
how are you?"""


greeting = '   Hello world      '
greeting.strip()  # same as trim()

greeting.upper()  # same as toUpperCase()
greeting.lower()  # same as toLowerCase()


greeting = "Hello World"
greeting.replace("H", "J")  # Jello World, replace ALL "H" with "J"


# placeholder variables, similar to using template literals
# My name is John and I am 36
txt = "My name is {name} and I am {age}".format(name='John', age=33)

# if you put a "f" in front of the string, it will look in the surrounding space for variables it can plugin so you can ommit the format() part
name = 'John'
age = 36
txt = f"My name is {name} and I am {age}"  # My name is John and I am 36
