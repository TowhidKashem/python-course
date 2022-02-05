# import a module or file
import my_module


# named imports, same as `import { julia } from 'people'`
# import only sepecific functions from a file
from my_file_name import say_hello, say_goodbye


# import aliases, same as `import { foo as bar } from 'foo'`
import foo as bar


# not recomended, but you can import all functions from a module like this, same as `import * from 'people'`
from people import *

######

# putting a file named `__init__.py` inside any folder turns it into a package

# utils/
#   - __init__.py
#   - currency
#   - array

# import the function `convert_currency` from the file `currency` inside the `utils` module
import utils.currency from convert_currency
import utils.array from random_value  # similar to above

# the `__init__.py` allows both of the above import statements to be grouped to the `utils` module

# a `__pycache__` folder is automatically created in the same folder, it contains compiled code so that python doesn't
# need to recompile it again the next time the code is ran without changes

######

# see all the things a package is exporting
import utils.currency
dir(utils.currency)


# by deault everything is exported in a package, to make certain things not exported use the `_` prefix
# for example lets say we're using a third party lib in our custom module:
import hashlib

def convert_currency():
    hashlib.md5()  # do something with the third party lib

dir(utils.currency)  # shows that both `hashlib` and `convert_currency` are exported


# if we don't want `hashlib` to be exported rewrite it with the prefix:
import hashlib as _hashlib

def convert_currency():
    _hashlib.md5()

dir(utils.currency)  # shows that only `convert_currency` is exported


# an even better way to control what's exported is to use the `__all__` variable
# at the top of the module under the imports put this line:
__all__ = ['convert_currency', 'format_currency'] # a list of function names being exported

dir(utils.currency)  # shows that only `convert_currency` and `format_currency` are exported


# the __all__ variable can also be placed in the `__init__.py` file similar to how an `index.js` is often used to 
# import funtions from files within it's parent folder and export them from 1 place so that they can all then be imported from the parent folder as root
from utils.currency import convert_currency
from utils.currency import format_currency

__all__ = ['convert_currency', 'format_currency']

######

# when a file is imported all the code in it is immediately executed, to prevent this use the `__name__` variable like so:
if __name__ == '__main__':
    print('hello')

# this code will only run if the file is ran directly e.g. `python3 my_file.py` not `import my_file`
# the default value for the built in `__name__` variable is '__main__' when the file is being run directly, otherwise it's the file name


################## installing third party packages ##################

# installs the package using pythons package manager "pip" system wide, same as `npm install -g <package>`
> pip install <package>


# to generate all dependencies for a package, same as creating a `package.json` file
> pip freeze > requirements.txt

# to install all dependencies for a package, same as running `npm install`
> pip install -r requirements.txt


### a better way though is to install and use `pipenv` because it automatically creates `Pipfile` and `Pipfile.lock` files ###

> sudo -H pip install -U pipenv # install pipenv

# init a project using a specific python version, same as `npm init`
# this will generate a `Pipfile` in the project folder but the actual virtual environment will be located on the system at `/Users/<username>/.local/share/virtualenvs/*`
# pipenv installs packages in a virtual environment, on a project by project basis and not globally on the user's machine
> pipenv --python <version>

# create the virtual environment, all future pipenv operations will be executed in this vm
# you can confirm that you're in the vm by checking the terminal line and seeing the project name prefixed to the line label in parentheses
> pipenv shell

> deactivate # exit the virtual environment shell

> pipenv install <package> # install a package, seperate package names with spaces to install multiple

> pipenv install -d <package> # installs a package as a dev dependency, same as `npm install -D <package>`

> pipenv install # installs all dependencies in the Pipfile, same as `npm install`

> pipenv uninstall <package> # uninstalls a package

# pipenv offers dependency tracking, running this command will display a list of all installed packages and their dependencies
> pipenv graph

# before deleting a project folder run this first to remove the virtual environment created by pipenv for the project
> pipenv --rm
