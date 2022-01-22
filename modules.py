# import module/file
import my_module


# named imports, same as "import { julia } from 'people'"
# import only sepecific functions from a file
from my_file_name import say_hello, say_goodbye


# import aliases, same as "import { foo as bar } from 'foo'"
import foo as bar


# not recomended, but you can import all functions from a module like this
from people import *
