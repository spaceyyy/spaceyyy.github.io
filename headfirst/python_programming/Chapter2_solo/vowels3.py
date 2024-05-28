#!python3
# vowels.py - A program that checks for vowels in a list and contains no duplicates
#             and prompts the user to type in a word.

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)
