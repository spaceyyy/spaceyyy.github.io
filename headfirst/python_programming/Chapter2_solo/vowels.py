#!python3
# vowels.py - A program that checks for vowels in a list

vowels = ["a", "e", "i", "o", "u"]
word = "Milliways"

for letter in word:
    if letter in vowels:
        print(letter)