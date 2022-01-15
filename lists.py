# lists = arrays

myList = [1, 2, 3, False, [4, 5, 6], 'hello']

myList[0]  # 1

myList[-1]  # 'hello', same as myList[myList.length - 1]

myList[1:3]  # [2, 3, False], select a range of items by index


len(myList)  # 6, same as myList.length

myList[0] + 1  # 2, but original list value is not mutated


# same as push()
myList.append('world')

myList.pop()  # 'world', myList is mutated


# insert "wow" at the first index
myList.insert(1, 'wow')

myList.remove('inserted')  # same as filter()'ing by value

"hello" in myList  # True, same as includes()
"world" not in myList  # True, same as !includes()
