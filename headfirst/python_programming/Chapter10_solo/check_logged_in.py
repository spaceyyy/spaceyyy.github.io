#!python3
# check_logged_in.py - A program to check if a web user has logged in.


def check_logged_in() -> bool:
    if 'logged_in' in session:
        return True
    return False
