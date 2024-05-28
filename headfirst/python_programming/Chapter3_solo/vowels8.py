#!python3
# vowels8.py - A program that uses the .intersection() set built-in function method

vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")

found = set(vowels.intersection(set(word)))

for vowel in found:
    print(vowel)
