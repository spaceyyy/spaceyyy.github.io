#!python3
# marvin.py - using a for loop and printing w/ an escape tab character

paranoid_android = "Marvin"
letters = list(paranoid_android)
for char in letters:
    print('\t', char)
