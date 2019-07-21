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
for i in range(19, 59):
    num = octagonal(i)
    octs.append([num % 100])
for i in range(21, 64):
    num = heptagonal(i)
    for j in range(len(octs)):
        if(octs[j][0] == int(num/100)):
            octs[j].append(num % 100)
for i in range(23, 71):
    num = hexagonal(i)
    for j in range(len(octs)):
        if(len(octs[j]) > 1 and octs[j][1] == int(num/100)):
            octs[j].append(num % 100)
for i in range(26, 82):
    num = pentagonal(i)
    for j in range(len(octs)):
        if(len(octs[j]) > 2 and octs[j][2] == int(num/100)):
            octs[j].append(num % 100)
for i in range(32, 99):
    num = square(i)
    for j in range(len(octs)):
        if(len(octs[j]) > 3 and octs[j][3] == int(num/100)):
            octs[j].append(num % 100)
for i in range(45, 141):
    num = triangle(i)
    for j in range(len(octs)):
        if(len(octs[j]) > 4 and octs[j][4] == int(num/100)):
            octs[j].append(num % 100)
for i in range(19, 55):
    num = octagonal(i)
    for j in range(len(octs)):
        if(len(octs[j]) == 6 and octs[j][5] == int(num/100)):
            print(octs[j], "Works")
print("---")
for item in octs:
    if(len(item) == 6):
        print(item)
print("---")
# alternatively

octs = []
for i in range(19, 59):
    num = octagonal(i)
    octs.append([int(num / 100)])
for i in range(21, 64):
    num = heptagonal(i)
    for j in range(len(octs)):
        if(octs[j][0] == int(num % 100)):
            octs[j].append(int(num / 100))
for i in range(23, 71):
    num = hexagonal(i)
    for j in range(len(octs)):
        if(len(octs[j]) > 1 and octs[j][1] == int(num % 100)):
            octs[j].append(int(num / 100))
for i in range(26, 82):
    num = pentagonal(i)
    for j in range(len(octs)):
        if(len(octs[j]) > 2 and octs[j][2] == int(num % 100)):
            octs[j].append(int(num / 100))
for i in range(32, 99):
    num = square(i)
    for j in range(len(octs)):
        if(len(octs[j]) > 3 and octs[j][3] == int(num % 100)):
            octs[j].append(int(num / 100))
for i in range(45, 141):
    num = triangle(i)
    for j in range(len(octs)):
        if(len(octs[j]) > 4 and octs[j][4] == int(num % 100)):
            octs[j].append(int(num / 100))
for i in range(19, 55):
    num = octagonal(i)
    for j in range(len(octs)):
        if(len(octs[j]) == 6 and octs[j][5] == int(num % 100)):
            print(octs[j], "Works")
print("---")
for item in octs:
    if(len(item) == 6):
        print(item)
        
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
