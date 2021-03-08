import os
import datetime




# either use tuples and zip function to connect the choices together
# ** DONT do this **
# items = (
#     'Ayylien (sometimes it will abduct people...)',
#     'A bag of opened chips',
#     'Jack in a box -- Peek a boo!',
# )
# prices = (80, 3, 20)
# item_prices = zip(items, prices)

# or use a dictionary -- this is clearer and easier
item_prices = {
    'Ayylien (sometimes it will abduct people...)': 80,
    'A bag of unfinished chips': 3,
    'Jack in a box -- Peek a boo!': 30,
}


def ask():
    selections = ""
    for index, (item, price) in enumerate(item_prices.items()):
        # looks like: 1. Ayylien (sometimes it will abduct people...) -- $80
        selections += "{index}. {item} -- ${price}\r\n".format(index=index + 1, item=item, price=price)

    # response = input("Shopkeeper Crazy says: What'cha want? \r\n" +
    #                  selections +
    #                  "{index}. Exit\r\n".format(index=len(item_prices) + 1) +
    #                  "Your choice: "
    #                  )
    # will look something like:
    # response = input("Shopkeeper Crazy says: What do you want to buy? \r\n " 
    #     "1. Ayylien (sometimes it will abduct people...) -- $80 \r\n " 
    #     "2. A bag of opened chips -- $3\r\n "
    #     "3. Jack in a box -- Peek a boo! $20\r\n "
    #     "4. Exit\r\n"
    #     "Your choice: "
    # )

    # use list comprehension
    choices = [
        "{index}. {item} -- ${price} \r\n ".format(index=str(ii + 1), item=item, price=str(price))
        for ii, (item, price) in enumerate(item_prices.items())
    ]

    response = input("Shopkeeper Crazy says: What'cha want? \r\n " +
                     "".join(choices) +
                     str(len(item_prices) + 1) + ". Exit\r\n" +
                     "Your choice: "
                     )

    # check if response is between 1 to (item_prices length + 2): this is another usage of the 'in' keyword
    # remember range doesn't include the ending number, so we will need to + 2 to include the 'exit' option
    if not response.isdigit() or not int(response) in range(1, len(item_prices) + 2):
        print("Shopkeeper Crazy says: HEYY, I don't have that.\r\n -------------------")
        # we call the ask function again and again until the user entered a valid option
        # We are using a technique called recursion here, ie a function calling itself 
        return ask()
    # -1 to match the index 
    return int(response) - 1


# helper function to write content to transactions.txt
def write_to_file(text: str):
    with open('transactions.txt', 'a') as file:
        file.write(text + '\r\n')


# helper function to add transaction records
def add_transaction(transaction: dict):
    time_now = datetime.datetime.now()
    write_to_file("{timestamp} - {item} (${price}), -- remaining balance: {balance}".format(
        timestamp=time_now,
        item=transaction.get('item'),
        price=transaction.get('price'),
        balance=transaction.get('balance')
    ))


def main():
    balance = 100

    #  to separate shopping instances
    write_to_file('----------------- New Visit ------------------')

    # keep running until user exit or go broke
    while True:

        # display balance
        # ask to buy an item
        print("You have ${balance} left".format(balance=balance))
        # ask user to make a choice
        index_selected = ask()

        # keep running until user select exit shop option (the last option is length of item_prices)
        if index_selected == len(item_prices):
            print("Goodbye")
            break

        # dict
        item_selected = tuple(item_prices.keys())[index_selected]
        price_selected = tuple(item_prices.values())[index_selected]

        # deduct balance after buying
        balance -= price_selected

        # if balance < 0 terminate the program
        if balance <= 0:
            print('Shopkeeper Crazy says: Ya broke ay?! Get out!!')
            break

        # record transaction
        add_transaction({
            "item": item_selected,
            "price": price_selected,
            "balance": balance,
        })


# __name__ is a special variable that the python interpreter sets before everything else runs
# it represents the current file name
# when we are running the current file as the main python script, __name__ will be "__main__"
# when we using the current file as a module, the __name__ variable will be the file name
# it is a good practise to include this check, as python will only run the code inside the 'if' statement if
# the current file is ran as the main script.
if __name__ == "__main__":
    main()
