# lists = arrays

my_list = [1, 2, 3, False, [4, 5, 6], 'hello']

my_list[0]  # 1

my_list[-1]  # 'hello', same as my_list[my_list.length - 1]

my_list[0:2]  # [1, 2], same as my_list.slice(0, 2)

my_list[0] + 1  # 2, but original list value is not mutated

# copy array
my_list_copy = my_list.copy()
# or
my_list_copy = my_list[:]

my_list.append('world')  # same as push()

# add to the end of a list, same as using spread operator
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])  # [1, 2, 3, 4, 5, 6]

my_list.pop()  # 'world', my_list is mutated

# insert "wow" at the first index
my_list.insert(1, 'wow')

my_list.remove('inserted')  # same as filter()'ing by value

del my_list[0]  # delete by index


# list comprehensions, same as <array>.map(num => num * 2)
nums = [1, 2, 3]
doubled_nums = [num * 2 for num in nums]  # [2, 4, 6]

# conditionals are also supported when added to the end
# double only the number "2" and return it as a new list
doubled_nums = [num * 2 for num in nums if num == 2]  # [4]


# but map() exists too
# must wrap the result in list() because it doesn't return a list by default
def multiply_by_two(num):
    return num * 2


list(map(multiply_by_two, nums))  # [2, 4, 6]

# [2, 4, 6], same as above but 1 liner with lambda
list(map(lambda n: n * 2, nums))

# ['1', '2', '3'], supplying the built-in str() function here:
list(map(str, nums))


# reduce(), available in functools package
# import functiontools
functools.reduce(lambda a, b: a + b, nums)  # 6


# make a shallow copy of the list (works on tuples as well)
# since it's shallow if the list had something like an object it will be a reference to it
copy = my_list[:]


my_list = [True, False, True]
any(my_list)  # True
all(my_list)  # False

# are all numbers greater than 0
my_list = [1, 2, 3, -5]
all([el > 0 for el in my_list])  # False


# same as Math.min() and Math.max()
min(my_list)  # -5
max(my_list)  # 3

# sort
sorted(['b', 'a', 'c'])  # ['a', 'b', 'c']
