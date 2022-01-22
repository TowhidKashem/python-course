# write, will create file if not exists
file = open('hello.txt', mode='w')
file.write('Hello World!\n')
file.close()  # always close the connection to avoid memory leaks


# append to the end of file's contents
file = open('hello.txt', mode='a')
file.write('Appended text!')
file.close()


# return file's contents as one large string
file = open('hello.txt', mode='r')
print(file.read())
file.close()


# return a list of strings for each line
file = open('hello.txt', mode='r')
print(file.readlines())
file.close()


# read each line one by one, can be used with a while loop to read all lines until there is none left
file = open('hello.txt', mode='r')
print(file.readline())
print(file.readline())
file.close()


# using this syntax is ideal because it will automatically close the file once the code in the block is done executing
# it also allows us to assign the file to a variable in one go
with open('hello.txt', mode='r') as file:
    print(file.read())
