# concatenate strings, same as js
name = 'John' + ' ' + 'Doe'

# repeat a string x times, same as 'hello'.repeat(10)
sayHelloTenTimes = 'Hello' * 10

# span mutiple lines with triple quotes, same as using backticks
# `greeting` will have \n for the line breaks in it
greeting = """hello
world
how are you?"""

# chars can be accessed by index or index ranges, same as lists
name = 'John'
name[0] = 'J'
name[1:2]  # "oh"


greeting = '   Hello world      '
greeting.strip()  # same as trim()

greeting.upper()  # same as toUpperCase()
greeting.lower()  # same as toLowerCase()


greeting = "Hello World"
greeting.replace("H", "J")  # Jello World, replace ALL "H" with "J"


# placeholder variables
age = 36
txt = "My name is John, and I am {}"
txt.format(age)
