#!python3
# nested_func.py - Gee, read the title...


def outer():
    def inner():
        print('This is inner.')

    print('This is outer, invoking inner.')
    inner()