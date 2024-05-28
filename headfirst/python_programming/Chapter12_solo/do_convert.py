#!python3
# do_convert.py - A file that converts military time into AM/PM

from datetime import datetime
import pprint


def convert2ampm(time24:str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

flights2 = {}
for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()

pprint.pprint(flights2)
print()


fts = {convert2ampm(k): v.title() for k, v in flights.items()}
print(fts)
print('\n')


just_freeport = {}
for k, v in flights.items():
    if v == 'FREEPORT':
        just_freeport[convert2ampm(k)] = v.title()
print(just_freeport)
print('\n')


# diction comprehension
just_freeport2 = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}
print(just_freeport2)
print('\n')


dests = set(fts.values())
print(dests)
print('\n')


wests = []
for k, v in fts.items():
    if v == 'West End':
        wests.append(k)
print(wests)
print('\n')


# list comprehension
wests2 = [k for k, v in fts.items() if v == 'West End']
print(wests2)
print()


for dest in set(fts.values()):
    print(dest, '->', [k for k, v in fts.items() if v == dest])
print('\n')


when = {}
for dest in set(fts.values()):
    when[dest] = [k for k, v in fts.items() if v == dest]
pprint.pprint(when)
print('\n')


# list comprehension in dictionary comprehension
when2 = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
pprint.pprint(when2)
print('\n')


vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget to pack a towel."

found = set()
for v in vowels:
    if v in message:
        found.add(v)
print(found)
print('\n')


# set comprehension
found2 = {v for v in vowels if v in message}
print(found2)