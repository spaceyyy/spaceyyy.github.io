#!python3
# myster.py - Do functiion arguments support by-value or by-reference
#             call semantics in Python?


def double(arg):            # Tom's value -> passed-by-value
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


def change(arg):            # Sarah's value-> passed-by-reference
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)

print(double([1, 2, 4]))    # added code for testing
print(change([1, 2, 4]))    # added code for testing
