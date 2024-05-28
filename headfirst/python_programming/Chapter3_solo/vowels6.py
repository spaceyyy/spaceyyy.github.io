#!python3
# vowels6.py - A program that causes a KeyError due to a key value not 
#              initialized so the interpreter can not increment a non-existing value

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

found = {}

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'times(s).')
