# lists = arrays

myList = [1, 2, 3, False, [4, 5, 6], 'hello']

myList[0]  # 1

myList[-1]  # 'hello', same as myList[myList.length - 1]

myList[0] + 1  # 2, but original list value is not mutated

myList.append('world')  # same as push()

myList.pop()  # 'world', myList is mutated

# insert "wow" at the first index
myList.insert(1, 'wow')

myList.remove('inserted')  # same as filter()'ing by value


# list comprehensions, same as <array>.map(num => num * 2)
nums = [1, 2, 3]
doubled_nums = [num * 2 for num in nums]  # [2, 4, 6]

# conditionals are also supported when added to the end
# double only the number "2" and return it as a new list
doubled_nums = [num * 2 for num in nums if num == 2]  # [4]
