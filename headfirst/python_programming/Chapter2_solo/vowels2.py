#!python3
# vowels.py - A program that checks for vowels in a list and contains no duplicates

vowels = ["a", "e", "i", "o", "u"]
word = "Milliways"
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)