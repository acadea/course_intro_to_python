# DONT DO THIS
# fruit1 = 'apple'
# fruit2 = 'orange'
# fruit3 = 'pineapple'
# fruit4 = 'durian'

# list is an array of data
fruits = ['apple', 'orange', 'pineapple', 'durian']

# access individual item by putting the item's index in the square bracket
print(fruits[0])  # expected: apple

# setting the element's value
# now the first element is banana
fruits[0] = 'banana'

# adding new item to the end of the list (in place ie change the object directly)
fruits.append('kiwi')
print(fruits)

# in place (change the object directly) sorting of fruits
fruits.sort()
print(fruits)

fruits.pop(0)  # delete index 0, ie banana

# Slicing
print(fruits[1:3]) # getting the second and third item, python will not include the ending index
print(fruits[0:5:2]) # getting 0th till 4th index, increment by 2
print(fruits[::3]) # getting 0th till the end, increment by 3
print(fruits[-1]) # getting the last element
print(fruits[::-1]) # increment by -1, ie reversing 

# tuple is the immutable (cannot be changed) version of list
vegetables = ('ginger', 'garlic', 'spinach', 'carrot')
print(vegetables[0])  # expected: ginger
 
# this will throw an error
# vegetables[0] = 'hey'



# set -- only allow unique values
balls = {'red', 'blue', 'red', 'purple'}
print(balls)

# string is also an immutable iterable
hey = 'hey there'
print(hey[0])  # expected: h

# this will throw an error
# hey[0] = 'p'


# Dictionary -- iterable with key and value pair
# key has to be immutable
dictionary = {
    'orange': 4,
    (21, 32): 6,
    # ['hey']: 9,   # this will throw an error, because list is mutable
    56: 9,
    56.31: 9,
}
print(dictionary)

print(dictionary['orange'])

# change the value of 'orange' from 4 to 'hey
dictionary['orange'] = 'hey'
