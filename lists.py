# lists = arrays

myList = [1, 2, 3, False, [4, 5, 6], 'hello']

myList[0]  # 1
len(myList)  # 6, same as myList.length

myList[0] + 1  # 2, but original list value is not mutated


# [1, 2, 3, False, [4, 5, 6], 'hello', 'world'], same as push()
myList.append('world')

myList.pop()  # 'world', myList is mutated

myList[-1]  # 'hello', same as myList[myList.length - 1]
