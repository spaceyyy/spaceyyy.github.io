#!python3
# change.py - A program for the debate b/w Tom and Sarah


def double(arg):    # Tom's code -> pass-by-value
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


def change(arg):    # Sarah's code -> pass-by-reference
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)


double([1, 2, 4])   # added code for testing
change([1, 2, 4])   # added code for testing