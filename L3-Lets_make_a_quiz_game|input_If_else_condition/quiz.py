import random

# user_name = input("What is your name?")
# password = input("Enter your password: ")
# print(user_name)
#
# if (user_name == 'sam' and password == '123') or user_name == 'admin':
#     print("Welcome Sam")
# else:
#     print("You are not Sam")

# random_number = random.randrange(1, 10)
#
# print(random_number)



# Goal: to write a math quiz

# generate 2 random numbers
first_number = random.randrange(1, 10)
second_number = random.randrange(1, 10)

# calculate the sum of these numbers (the actual answer)
quiz_answer = first_number + second_number

# ask the user the question
# \r -- special character: return carriage
# \n -- special character: line break
user_input = input("What is " + str(first_number) + " + " + str(second_number) + "? \r\n")

# compare the user input with the actual answer
# print out the result
if user_input == str(quiz_answer):
    print("Yay! You are correct!")
elif user_input == "":
    print("You didn't even try...")
else:
    print("OOPS, the correct answer is: " + str(quiz_answer))



