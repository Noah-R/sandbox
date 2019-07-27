def gcfOfOne(a, b):
    gcf=1
    for c in range(2, int((b**.5)+1)):
        if(a%c==0 and b%c==0):
            return False
    return True
#https://projecteuler.net/problem=71
answer=[0,0]
greatest=0
for d in range(2, 1000000):
    if(d%10000==0):
        print(d)
    for n in range(int(d*.428571), int(d*.428572)+1):
        if(gcfOfOne(d, n)):
            frac=n/d
            if(frac>greatest and frac<3/7):
                greatest=frac
                answer=[n, d]
print(answer)
"""
The below solution is better
But the above solution works too
"""
place=1
numer=1
denom=3
frac=1/3
for d in range(4, 1000000):
    newfrac=(place+1)/d
    if(newfrac<3/7):
        place+=1
        if(newfrac>frac):
            frac=newfrac
            numer=place
            denom=d
print(numer)