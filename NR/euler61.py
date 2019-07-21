# https://projecteuler.net/problem=61


def triangle(n):
    return n*(n+1)/2


def iswhatever(n, method):
    i = 0
    while(True):
        result = method(i)
        if(result == n):
            return True
        if(result > n):
            return False
        i += 1


def square(n):
    return n*n


def pentagonal(n):
    return n*(n*3-1)/2


def hexagonal(n):
    return n*(2*n-1)


def heptagonal(n):
    return n*(5*n-3)/2


def octagonal(n):
    return n*(3*n-2)


for i in range(4000):
    start = 0
    if(start == 0 and len(str(triangle(i))) == 4):
        start = i
        print("Triangles start at", start)
    elif(start > 0 and len(str(triangle(i))) == 5):
        print("Triangles end at", i)
        break

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
                            if(iswhatever(l[1], square)):
                                if(iswhatever(l[2], pentagonal)):
                                    # if(iswhatever(l[3], hexagonal)):
                                    #    if(iswhatever(l[4], heptagonal)):
                                    #        if(iswhatever(l[5], octagonal)):
                                    print(l)
                        for z in range(5):
                            l.append(l.pop(0))
                            if(iswhatever(l[0], triangle)):
                                if(iswhatever(l[1], square)):
                                    if(iswhatever(l[2], pentagonal)):
                                        # if(iswhatever(l[3], hexagonal)):
                                        #    if(iswhatever(l[4], heptagonal)):
                                        #        if(iswhatever(l[5], octagonal)):
                                        print(l)
"""
