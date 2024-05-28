#!python3
# try_examples3.py - An example using the `try/except` code with multiple
#                    `except` statements.


try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing.')
except PermissionError:
    print('This is not allowed.')