#!python3
# vowels7.py - File from last chapter, reusing it to show how to 
#              implement it into a function for the file vsearch
#              .py


vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)