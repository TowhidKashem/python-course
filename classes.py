# define class
class MyClass:
    # this is a class wide attribute, meaning all instances of this
    # class will share this attribute, if it's changed by one instance
    # it will propagate to all instances to the other, we should avoid these
    name = 'John'

    # all functions have the `self` argyment passed in, it's the same as `this`
    def say_hello(self):
        print('Hello ' + self.name)  # Hello John


# instantiate
p1 = MyClass()


# access properties and methods
print(p1.name)  # John


# define 'init' method, same as a 'constructor'
# arrtibutes defined inside the constructor are only available
# on an instance by instance basis
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# create new class 'Student' by extending 'Person'
class Student(Person):
    name = 'TK'
