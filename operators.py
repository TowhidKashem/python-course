# 'is' and 'is not' can be used to check if 2 things are references to the same object in memory
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a is b  # False
c is a  # True

a is not b  # True


is_dog and is_pet  # same as &&

is_dog or is_cat  # same as ||

# use 'not' to reverse the value
num = 10
not(num > 20)  # True, same as !(num > 20)
