# REMEMBER
# functions take in argument(s)
# do some processing
# and return the output

# function accepts no argument
def heyyey():
    print("heyyeyaaeyaaaeyaeyaa!!!!")

# function accepts one argument
def say(word):
    print(word)

# function accepts multiple argument
def add(x, y):
    return x + y

# function with type hint
def minus(x: float, y: float):
    return x - y

# function with optional arguments
def calculate_tax(revenue: float, tax_rate: float = 0.1):
    return revenue * tax_rate

# function with multiple optional arguments
def create_ayylien(planet="The Zone", size="big", colour="blue", hobby="abduct"):
    abc = add(2,4)

    print('The ayylien comes from ', planet)
    print("Size: ", size)
    print("Colour: ", colour)
    print("Hobby: ", hobby)

    print(abc)

# create_ayylien()
# print(added)

# create_ayylien(hobby="play football")
# create_ayylien(hobby="play football", size="big")

# print(add(1,4))
# print(minus(9,4))
# print(calculate_tax(100))




