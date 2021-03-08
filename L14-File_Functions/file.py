# https://www.programiz.com/python-programming/file-operation
import os

# make dir
# getcwd() -> get current working directory
cwd = os.getcwd()
path = cwd + '/notes'

# creating folder
try:
    os.mkdir(path=path)
except FileExistsError as e:
    # if directory already exist, will raise file exist error
    # don't need to do anything. the pass keyword will pass on to the next block of code
    pass

# deleting folder
# try:
#     os.rmdir(path=path)
# except FileNotFoundError as e:
#     # if directory does not exist, will raise file not found error
#     pass


# to use try finally block is because if an exception occurs, we can guarantee the file operation will be closed
file_path = path + "/notes.txt"

# mode r --> read
# mode w --> write
# mode a --> append
file = open(file_path, mode='w')
# operation..
# ...
file.write("extraa longgg textt")
file.close()

# Why do we want to close the file?
# ans: to prevent memory leak
# memory leak is the idea of a program over-consumes the computer's memory
# ie consumes more memory than necessary
# this is bad because memory leak can drain the computer's memory and freeze the computer

# everytime python opens a file, it creates a new process
# Although python will try to clean unused resources, it is not guaranteed
#


# or better: this will ensure the file is closed when the clock inside 'with' is exited
# writing to file, will overwrite the content
with open(file_path, mode='w') as file:
    file.write("heya \r\n")
    file.write("heya2 \r\n")
    file.write("heya3 \r\n")

# updating file
with open(file_path, mode='a') as file:
    file.writelines([
        'haha\n',
        'hehe\n',
        'hoho\n',
    ])

# reading file line by line
with open(file_path, mode='r') as file:
    for line in file:
        print(line)

# deleting file
os.remove(path=file_path)
