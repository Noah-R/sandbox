#https://projecteuler.net/problem=72
def gcfOfOne(a, b, primes):
    index=0
    while(primes[index]<int((b**.5)+1)):
        c=primes[index]
        if(a%c==0 and b%c==0):
            return False
        index+=1
    return True
f=open("primes1.txt", 'r')
primes=eval(f.read())
primebuckets=[]
for a in range(1000000):
    primebuckets.append(False)
for a in primes:
    primebuckets[a]=True
count=0
for d in range(1, 1000000):
    if(d in primes):
        count+=d-1
    else:
        for n in range(d):
            if(primebuckets[n] or gcfOfOne(n, d, primes)):
                count+=1
    if(d%1000==0):
        print(d)
print("Count",count)