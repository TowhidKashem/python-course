# outputs all the methods and properties avaiable in a data structure, class, etc
help([])
help(MyClass)


# print all the properties and methods of a module
print(dir(my_module))


# same as `typeof`
type('abc')  # str
type(10)  # int
type(1.5)  # float
type([1, 2, 3])  # list
type(("apple", "banana", "cherry"))  # tuple
type({"name": "John", "age": 36})  # dict
type(True)  # bool
