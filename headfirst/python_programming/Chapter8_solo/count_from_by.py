#!python3
# count_from_by.py - A file that is an introduction to Classes


class CountFromBy:

    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)


# Added code below for testing
k = CountFromBy()
print(k)

print()

k.increase()
print(k)

print()

l = CountFromBy(100)
print(l)
print()

l.increase()
print(l)

m = CountFromBy(100, 10)
print(m)
m.increase()
print(m)
print()

n = CountFromBy(i=15)
print(n)
n.increase()
print(n)
