# round brackets are optional when creating a tuple
# But it is good to put the round bracket for clarity
c = 90, 100
print(c)

# tuple destructuring -- aka unpacking tuple
# creating multiple variables in one go
# we usually use an underscore variable if we don't want an element (just a convention)
# *c pack the rest of tuple as a list into the variable c
a, b, _, *c = (50, 100, 150, 200, 250)

print(a)  # 50
print(b)  # 100
print(c)  # [200, 250]


# How can destructuring be useful?
# traditionally we need to do: (tedious)
# temp = a
# a = b
# b = temp

# swap variable values
a, b = b, a

# looping dictionary
fruit_prices = {
    'orange': 4,
    'apple': 6,
    'durian': 9,
    'kiwi': 10,
}

for fruit in fruit_prices:
    print(fruit)

# .items() will pack the entries into tuple of key and value
for fruit in fruit_prices.items():
    print(fruit)

# for each iteration, we can unpack the tuple by destructuring
for fruit, price in fruit_prices.items():
    print(fruit, price)


# more dict function
# the .get() function
# when value is not present, will return None instead of python terminating program and throwing an error

print(fruit_prices.get("apple"))
# print(fruit_prices.get("apple1"))  # return None
# print(fruit_prices["apple1"])  # throws error

# or supply a default value
print(fruit_prices.get('apple', 20))

# .update() will update the value of a key in a dict
# if the key is not present, will just create it
print(fruit_prices.update({"apple": 100}))

# gets all the keys in a dict as an iterable
print(fruit_prices.keys())
# gets all the values in a dict as an iterable
print(fruit_prices.values())

# enumerate function: getting index and value when looping thru list/tuple
for index, value in enumerate(['hey', 'ho', 'ya']):
    print(index, value)

# zip function pair up items in 2 iterable
first_names = ['pinky', 'cindy', 'crazy', 'randy']
last_names = ['funky', 'dashy', 'trashy', 'fishy']
for first_name, last_name in zip(first_names, last_names):
    print("Full name is: " + first_name + ' ' + last_name)

# list comprehension
incomes = [100, 150, 200, 130, 400]

# goal: create a new list with tax 10% deducted from the income

# first way (traditional way)
after_taxed = []

for income in incomes:
    after_taxed.append(income * 0.9)

# list comprehension (could be very hard to read when the logic is complex)
after_taxed = [income * 0.9 for income in incomes]

# list comprehension is chainable
payrolls = {
    "crazy": [100, 150, 200, 130, 400],
    "dazzy": [108, 250, 202, 110, 50],
    "cranky": [428, 650, 22, 130, 50],
}

# to calc net income for all wages
net_income = [income * 0.9 for incomes in payrolls.values() for income in incomes]
print(net_income)

# to group the income by person
net_income_group = [[income * 0.9 for income in incomes] for incomes in payrolls.values()]
print(net_income_group)

# creating a dict containing net income for everyone
net_income = {person: [income * 0.9 for income in incomes] for person, incomes in payrolls.items()}
print(net_income)
