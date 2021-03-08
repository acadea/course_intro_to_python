# __init__.py is the entry point of every module
# if we put a __init__.py file in a folder, python will recognise
# the folder as a module
import random

# we use the 'from' keyword to specify module path
# dot '.' tells python to look for the module in the current dir
# double dots '..' tells python to look for the module in the parent dir
# without dot will tell python to look for built-in / third party modules installed in our system

# 'import' keyword to import a particular symbol from the module
# if we want to import multiple symbols, we use comma to separate the imports

# renaming quotes as _quotes to declare it as private symbol
from ._quotes import quotes as _quotes


def inspire():
    return random.choice(_quotes)


# count the total number of quotes available
def count():
    return len(_quotes)
