import random
fruits = ['apple', 'orange', 'pineapple', 'durian']

# DONT DO THIS
# print("I love " + fruits[0])
# print("I love " + fruits[1])
# print("I love " + fruits[2])
# print("I love " + fruits[3])

# for fruit in fruits:
#     print("I love " + fruit)
#
# # for ii in range(3):
# #     print("Current number is: " + str(ii))
#
# for ii in range(len(fruits)):
#     print("I LOVE " + fruits[ii])

# exercise: loop thru all type of iterable, eg set, tuple, string and dict

# Goal: make a number guessing game

# randomly pick a number between 1 and 10 as the answer
answer = random.randrange(1, 10)
# ask the player to pick a number
guess = input("Pick a number between 1 - 10: ")
# if player failed to guess the answer, repeat until succeed
while (guess != str(answer)):
    guess = input("Try again...you need to pick again :) : ")

print("Yay! It is correct!")
