# convert to boolean value
name = 'Joe'
bool(name)  # True bc "name" exists, same as Boolean(name)
bool(0)  # False


name = None  # same as null
if name:
    print('yes')
else:
    print('no')  # no
