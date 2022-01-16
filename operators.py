# 'is' and 'is not' can be used to check if 2 things are references to the same object in memory
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a is b  # False
c is a  # True

a is not b  # True


[1, 2, 3] == [1, 2, 3]  # True, can compare the VALUES of 2 lists like this unlike js
[1, 2, 3] is [1, 2, 3]  # False, they're still different objects in memory


if is_dog and is_pet  # same as &&

if is_dog or is_cat  # same as ||


# can group conditions with parentheses
if (is_dog and is_pet) or (is_cat and is_pet)


# use 'not' to reverse the value
num = 10
not(num > 20)  # True, same as !(num > 20)
