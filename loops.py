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

# loop from 6 to 12, same as for (let i = 6; i < 12; i++)
for x in range(6, 12):
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

# or use enumerate() for easy access to the index
for (index, value) in enumerate(fruits):
    print(index)  # 0, 1, 2
    print(value)  # apple, banana, cherry


# jump iterations by more than 1, the optional 3rd agument in range() is the "step"
for fruit_index in range(len(fruits), 2):
    print(fruits[fruit_index])  # jumps to every 2nd element


# get key and value in dict
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for key, value in car.items():
    print(key, value)  # (brand, Ford), (model, Mustang), (year 1964)


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
