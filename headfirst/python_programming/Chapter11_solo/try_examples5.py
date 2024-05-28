#!python3
# try_examples5.py - Using a `try/except` statement with Exception error `as`
#                    `err` and print out `Exception` catch-all error.


try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing.')
except PermissionError:
    print('This is not allowed.')
except Exception as err:
    print('Some other error occurred:', str(err))
