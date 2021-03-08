import random

# Defining the rewards
ayylien = '''
░░░░░░░░▄██████▄
░░░░░░░█▀▀▀██▀▀▀▄
░░░░░░░█▄▄▄██▄▄▄█           U HAVE BEEN ABDUCTED BY
░░░░░░░▀█████████
░░░░░░░░▀███▄███▀░░         THE AYYLIEN
░░░░░░░░░▀████▀░░░░░
░░░░░░░▄████████▄░░░░ 
░░░░░░████████████░░░░ 
'''

grand_prize = '10m cash!!'
toilet_paper = 'A 10x5 cm piece of toilet paper found in a public toilet.'


# the main function to play for a round
def play_monty_hall():
    # create a list of rewards
    rewards = [grand_prize, ayylien, toilet_paper]

    # randomise the order of rewards
    random.shuffle(rewards)

    # create a choices list, eg [0, 1, 2] to keep track of the choices number
    choices = list(range(3))

    selected = input("Welcome to the Luckyyy Draw. You could win 10m cash!! Pick a reward -- Select 1, 2 or 3: ")

    # we validate the user input to only allow 1 2 or 3

    # tedious
    # if not (selected == '1' or selected == '2' or selected == '3'):

    # better to use the 'in' operator
    if not (selected in ('1', '2', '3')):
        # stop the program is user enter something else
        exit("Opps..You can only pick 1, 2 or 3. Try again next time.")

    # selected from user input is a string, so we should convert it to integer
    # pop() removes the user selected choice from the choices and rewards list
    choices.pop(int(selected) - 1)
    prize_selected = rewards.pop(int(selected) - 1)

    # we randomise the item to be revealed
    to_reveal_index = random.randrange(0, len(rewards))

    # check if to reveal is grand prize or not, if yes, we should reveal the other one
    # at this point we only have 2 rewards left in the reward list, (user selected reward has already been removed)
    # subtracting 1 from to_reveal_index will always ensure we get the other reward
    # eg if "to_reveal_index" is randomised to 0, it will turn into -1, which will be the last element 
    # eg if "to_reveal_index" is randomised to 1, it will turn into 0, which will be the first element 
    if rewards[to_reveal_index] == grand_prize:
        to_reveal_index = to_reveal_index - 1

    to_reveal = rewards.pop(to_reveal_index)

    # we should + 1 to the choices, remember choices is a list consisting of [0, 1, 2]
    print("-------------------------------------------------")
    to_change = input("Number " + str(choices[to_reveal_index] + 1) + " is.....\r\n" +
                      to_reveal + "\r\n" +
                      "Do you wish to change your selection? Enter 'y' to switch, otherwise any other key to continue.")

    # converting user input to lowercase just in case user put in Capital case
    if to_change.lower() == 'y':
        # we only have 1 price left
        prize_selected = rewards[0]

    print("Congratulation!! You have won....\r\n" + prize_selected)


def main():
    while True:
        play_monty_hall()

        # anything in the if condition will be executed and evaluated
        # that means we can incorporate our input function inside it
        # we convert the input to lowercase incase player typed in capital Y
        # if player entered anything other than Y, we will break the while loop
        if input("Press y to play again. answer: ").lower() != 'y':
            print("Goodbye. See you again next time!")
            break


if __name__ == "__main__":
    main()
