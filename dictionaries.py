# dictionaries don't guarantee insertion order, keys are unique

# keys must be wrapped in quotes, unlike js it's not optional
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.get('model')  # Mustang
car['model']  # Mustang

car["brand"] = "Mercedes"  # update or add new values

car.pop('model')  # remove the model key/value pair

car.clear()  # empty the dictionary "{}"

car.copy()  # make a copy, same as "newCar = { ...car }"

# convert a list of tuples into a dictionary using dict comprehensions
stats = [('age', 22), ('height', 5.9), ('weight', 170)]
dict_stats = {key: value for (key, value) in stats}

print(dict_stats)  # {'age': 22, 'height': 5.9, 'weight': 170}


del car['brand']  # delete by key


# for ordered dictionaries, use OrderedDict from the `collections` package
# it takes a list of tuples and returns an ordered dictionary
collections.OrderedDict([('name', 'TK'), ('age', 33)])


# import json
json.dumps(dict)  # same as `JSON.stringify(dict)`
json.loads(str)  # same as `JSON.parse(str)`


# convert a class into a dictionary
print(self.__dict__)  # from the inside

# or from the outside
my_class = MyClass()
print(my_class.__dict__)
