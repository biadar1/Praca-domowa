import itertools as it
#zadanie10
def zadanie10():
    a=(x for x in it.permutations(range(0,10),3))
    print(a)
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
#zadanie11
def zadanie11(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b 
f=zadanie11(10)
print(f)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))