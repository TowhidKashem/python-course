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


# for else
for fruit in fruits:
    print(fruit)
else:
    print("all done!")


# to get the index either keep a counter and increment it manually or use the range() function
manual_index_counter = 0
for fruit_index in range(len(fruits)):
    print(fruits[fruit_index])
    print(manual_index_counter)
    manual_index_counter += 1


# jump iterations by more than 1, the optional 3rd agument in range() is the "step"
for fruit_index in range(len(fruits), 2):
    print(fruits[fruit_index])  # jumps to every 2nd element


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
