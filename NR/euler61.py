# https://projecteuler.net/problem=61


def triangle(n):  # 45 to 141
    return int(n*(n+1)/2)


def iswhatever(n, method):
    i = 0
    while(True):
        result = method(i)
        if(result == n):
            return True
        if(result > n):
            return False
        i += 1


def square(n):  # 32 to 99
    return n*n


def pentagonal(n):  # 26 to 81
    return int(n*(n*3-1)/2)


def hexagonal(n):  # 23 to 70
    return n*(2*n-1)


def heptagonal(n):  # 21 to 63
    return int(n*(5*n-3)/2)


def octagonal(n):  # 19 to 58
    return n*(3*n-2)


octs = []
hepts = []
hexes = []
pents = []
squares = []
tris = []
works = [octs, hepts, hexes, pents, squares, tris]
sequences = []
for a in range(6):
    for b in range(6):
        for c in range(6):
            for d in range(6):
                for e in range(6):
                    for f in range(6):
                        l = [a]
                        if(b not in l):
                            l.append(b)
                        if(c not in l):
                            l.append(c)
                        if(d not in l):
                            l.append(d)
                        if(e not in l):
                            l.append(e)
                        if(f not in l):
                            l.append(f)
                        if(len(l) == 6):
                            sequences.append(l)
for i in range(19, 59):
    num = octagonal(i)
    octs.append(num)
for i in range(21, 64):
    num = heptagonal(i)
    hepts.append(num)
for i in range(23, 71):
    num = hexagonal(i)
    hexes.append(num)
for i in range(26, 82):
    num = pentagonal(i)
    pents.append(num)
for i in range(32, 99):
    num = square(i)
    squares.append(num)
for i in range(45, 141):
    num = triangle(i)
    tris.append(num)
for sequence in sequences:
    for a in works[sequence[0]]:
        for b in works[sequence[1]]:
            if(a % 100 == int(b/100)):
                for c in works[sequence[2]]:
                    if(b % 100 == int(c/100)):
                        for d in works[sequence[3]]:
                            if(c % 100 == int(d/100)):
                                for e in works[sequence[4]]:
                                    if(d % 100 == int(e/100)):
                                        for f in works[sequence[5]]:
                                            if(e % 100 == int(f/100) and f % 100 == int(a/100)):
                                                print(
                                                    "Answer:", a+b+c+d+e+f)