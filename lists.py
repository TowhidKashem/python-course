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
