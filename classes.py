# define class
class MyClass:
    # this is a class wide attribute
    name = 'John'

    # all methods in a class needs the `self` argument passed in, it's the same as `this`
    def say_hello(self):
        print('Hello ' + self.name)  # Hello John


# instantiate
p1 = MyClass()


# access properties and methods
print(p1.name)  # John


# define 'init' method, same as 'constructor'
# arrtibutes defined inside the constructor are only available
# on an instance by instance basis
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # private properties are defined with a `__` in front of the name
        # these can only be accessed from other methods in the class and never from outside the class
        self.__private_name = 'secret'

    def print_private_name(self):
        print(self.__private_name)


person = Person('TK', 33)

print(person.name)  # tk
# print(person.__private_name)  # will throw error
print(person.print_private_name())  # secret

# convert the class to a dictionary, helpful for viewing when debugging, only includes the properties not methods
print(person.__dict__)


# create new class 'Student' by extending 'Person'
class Student(Person):
    hobby = 'swimming'

    def __init__(self, name, age, grade):
        # all extended classes need to call super() otherwise it's constructor is overriding the parent's
        super().__init__(name, age)
        self.grade = grade

    # this built in method can be used to display custom output when the class is printed, useful for debugging
    def __repr__(self):
        return 'custom output here...'

    # methods that don't need access to any other class attritbute can be labeled with the @staticmethod decorator
    # these methods will error if self is passed in as an argument since they only use any arguments passed into them from the place where they're called (if any)
    @staticmethod
    def say_hello(name):
        print('Hello ' + name)

    # methods that only need to access class level properties can be labeled with the @classmethod decorator
    # it's a convention to name the argument that's passed in as "cls", it's different from "self" in that
    # it only gives access to class level properties (including the parent's) and not to any properties or methods elsewhere such as those defined in the constructor
    @classmethod
    def print_hobby(cls):
        print(cls.hobby)


student = Student('TK', 33, 9)

print(student.name)  # tk (comes from base class)
print(student.grade)  # 9 (comes from current class)
print(student)  # custom output here...

print(student.say_hello('Joe'))  # Hello Joe
print(student.print_hobby())  # swimming

# static and class methods can also be called directly WITHOUT instantiating the class first
print(Student.say_hello('Sam'))  # Hello Sam
print(Student.print_hobby())  # swimming
