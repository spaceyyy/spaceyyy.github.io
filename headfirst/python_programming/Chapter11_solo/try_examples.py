#!python3
# try_examples.py - An example using `with`.


with open('myfile.txt') as fh:
    file_data = fh.read()
print(file_data)