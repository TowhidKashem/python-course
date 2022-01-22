# lists = arrays

myList = [1, 2, 3, False, [4, 5, 6], 'hello']

myList[0]  # 1

myList[-1]  # 'hello', same as myList[myList.length - 1]

myList[0:2]  # [1, 2], same as myList.slice(0, 2)

myList[0] + 1  # 2, but original list value is not mutated

myList.append('world')  # same as push()

# add to the end of a list, same as using spread operator
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])  # [1, 2, 3, 4, 5, 6]


myList.pop()  # 'world', myList is mutated

# insert "wow" at the first index
myList.insert(1, 'wow')

myList.remove('inserted')  # same as filter()'ing by value

del myList[0]  # delete by index


# list comprehensions, same as <array>.map(num => num * 2)
nums = [1, 2, 3]
doubled_nums = [num * 2 for num in nums]  # [2, 4, 6]

# conditionals are also supported when added to the end
# double only the number "2" and return it as a new list
doubled_nums = [num * 2 for num in nums if num == 2]  # [4]


# make a shallow copy of the list (works on tuples as well)
# since it's shallow if the list had something like an object it will be a reference to it
copy = myList[:]


myList = [True, False, True]
any(myList)  # True
all(myList)  # False

# are all numbers greater than 0
myList = [1, 2, 3, -5]
all([el > 0 for el in myList])  # False
