try:
    open('path/to/non/existing/file.txt')
except IOError:
    print('File does not exist.')


# can specify multiple errors via comma seperated list
try:
    open('path/to/non/existing/file.txt')
except (IOError, ValueError):
    print('File does not exist.')


# can specify multiple errors via further except blocks
try:
    open('path/to/non/existing/file.txt')
except (IOError):
    print('File does not exist.')
except (ValueError):
    print('A value error has occured.')


# can chain finally blocks too
try:
    open('path/to/non/existing/file.txt')
except (IOError):
    print('File does not exist.')
finally:
    print('Done!')
