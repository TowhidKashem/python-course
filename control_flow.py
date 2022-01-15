# if
if a != b:
    print("a is not equal to b")


# if else
if a == b:
    print("a is equal b")
else:
    print("a is not equal b")


# if elseif else
if a == b:
    print("a is equal b")
elif a > b:
    print("a is greater than b")
else:
    print("hmmm")


# shorthand if else
print("Yes") if 5 > 2 else print("No")


# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if (fruit == 'apple'):
        continue
    if (fruit == 'banana'):
        break
    print(fruit)


# loop 6 times, same as for (let i = 0; i < 6; i++)
for x in range(6):
    print(x)


# while
i = 1
while i < 6:
    print(i)
    if (i == 4):
        continue
    if (i == 3):
        break
    i += 1


# while else
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
