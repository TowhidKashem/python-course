# define class
class MyClass:
    x = 5


# instantiate
p1 = MyClass()


# access properties and methods
print(p1.x)


# define 'init' method, equivalent to a 'constructor', the first argument of 'self' is required
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# create new class 'Student' by extending 'Person'
class Student(Person):
    name = 'TK'
