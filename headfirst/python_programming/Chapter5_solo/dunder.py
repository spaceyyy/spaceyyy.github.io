#!python3
# dunder.py - a dunder program that displays where the program code
#             is executed, either in Python or Python Shell prompt
#             (command line)


print('We start off in:', __name__)
if __name__ == '__main__':
    print('And end up in:', __name__)
