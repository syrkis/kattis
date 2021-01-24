from sys import stdin

n = int(stdin.readline())

D = {}

def dera(n): 
    if n <= 0:
        return 1
    return (n - 1) * (dera(n - 1) + dera(n - 2))

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

if n >= 10:
    print(1 - (dera(10) / fact(10)))
else:
    print(1 - (dera(n) / fact(n)))
