# will throw exception because we are accessing an index out of range
# numbers = [1, 2, 6]
# numbers[3]

def say(word):
    # raise IndexError('random error here')

    if type(word) != str:
        raise ValueError("Word must be type of string")
    print(word)

# say(123)

try:
    say(123)
# except Exception will catch all exception
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("Finally!")  # will run no matter what

# https://docs.python.org/3/library/exceptions.html#exception-hierarchy