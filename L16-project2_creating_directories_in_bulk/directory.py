import os

# configuration

# get current directory path
PATH = os.getcwd()
# define the total number of folder to be created
NUM_OF_FOLDER = 12
# prefix of folder name
PREFIX = "week_"
# postfix of folder name
POSTFIX = ""


def main():
    # create directories for X number of times as defined in the config
    # adding 1 to NUM_OF_FOLDER since we starts from 1
    for ii in range(1, NUM_OF_FOLDER + 1):
        # creating folder eg week_1, week_2 ...
        create_dir(PATH + '/' + file_name(str(ii)))


def file_name(name: str):
    # generating file name by adding prefix and suffix
    return PREFIX + name + POSTFIX


def create_dir(path):
    try:
        os.mkdir(path=path)
    except FileExistsError:
        pass


if __name__ == '__main__':
    main()
