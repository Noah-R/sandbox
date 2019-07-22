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
hepts=[]
hexes=[]
pents=[]
squares=[]
tris=[]
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
print("---")
print(octs)
print(hepts)
print(hexes)
print(pents)
print(squares)
print(tris)
        
"""This code theoretically checks them all but it takes too long and it doesn't work anyway
for a in range(10, 100):
    print(a)
    for b in range(10, 100):
        for c in range(10, 100):
            for d in range(10, 11):
                for e in range(10, 11):
                    for f in range(10, 11):
                        num1 = a*100+b
                        num2 = b*100+c
                        num3 = c*100+d
                        num4 = d*100+e
                        num5 = e*100+f
                        num6 = f*100+a
                        l = [num1, num2, num3, num4, num5, num6]
                        if(iswhatever(l[0], triangle)):
                            if(iswhatever(l[1], pentagonal)):
                                if(iswhatever(l[2], pentagonal)):
                                    # if(iswhatever(l[3], hexagonal)):
                                    #    if(iswhatever(l[4], heptagonal)):
                                    #        if(iswhatever(l[5], octagonal)):
                                    print(l)
                        for z in range(5):
                            l.append(l.pop(0))
                            if(iswhatever(l[0], triangle)):
                                if(iswhatever(l[1], pentagonal)):
                                    if(iswhatever(l[2], pentagonal)):
                                        # if(iswhatever(l[3], hexagonal)):
                                        #    if(iswhatever(l[4], heptagonal)):
                                        #        if(iswhatever(l[5], octagonal)):
                                        print(l)
"""
