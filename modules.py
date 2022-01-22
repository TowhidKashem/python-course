# import module
import mymodule


# named imports, same as import { julia } from 'people'
from julia import people


# import aliases, same as import { foo as bar } from 'foo'
import foo as bar


# print all the properties and methods of a module
print(dir(mymodule))
