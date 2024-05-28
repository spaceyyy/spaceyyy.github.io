#!python3
# mystery2.py - Do function arguments support by-value or by-reference
#               call semantics in Python?, adding print(id(arg))


def double(arg):
    print('Before: ', arg)
    print(id(arg))
    arg = arg * 2
    print('After: ', arg)
    print(id(arg))


def change(arg):
    print('Before ', arg)
    print(id(arg))
    arg.append('More data')
    print('After: ', arg)
    print(id(arg))

double([1, 2, 4])   # added code for testing
change([1, 2, 4])   # added code for testing