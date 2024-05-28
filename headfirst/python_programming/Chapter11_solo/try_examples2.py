#!python3
# try_examples2.py - An example using the `try/except` statement.


try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing.')