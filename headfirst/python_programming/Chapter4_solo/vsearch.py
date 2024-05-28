#!python3
# vsearch.py - A program using vowels7.py from last chapter in a function.


def search_for_vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_for_letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

print(search_for_vowels('hello'))   # added code for testing
print(search_for_letters('hello'))  # added code for testing
print(search_for_letters('hello', 'l'))  # added code for testing
