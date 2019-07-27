#https://projecteuler.net/problem=65
sequence=[2]
for i in range(1, 50):
    sequence.append(1)
    sequence.append(2*i)
    sequence.append(1)
num="2"
print (float(num))
def findlastnum(s):
    active=False
    start=0
    end=0
    for i in range(len(s)):
        nums=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if(s[i] in nums):
            end=i
            if(not active):
                start=i
                active=True
        else:
            active=False
    return [start, end]
def solve(s):
    print("start:",s)
    plus=s.find("+")
    fraction=s[plus+1:-1]
    addint=int(s[1:plus])
    div=fraction.find("/")
    numer=int(fraction[:div])
    denom=fraction[div+1:]
    if("/" in denom):
        print(numer,"over",denom)
        t=denom.find("/")
        numer=numer*denom[t+1:]
        denom=denom[:t]
        print("ends as",numer,"over",denom)
    numer=int(numer)
    denom=int(denom)
    end=str(addint*denom+numer)+"/"+str(denom)
    print("end",end)
    return end
for i in range(1,100):
    x=findlastnum(num)
    start=x[0]
    end=x[1]
    num=num[:start]+"("+num[start:end+1]+"+1/"+str(sequence[i])+")"+num[end+1:]
while("(" in num):
    start=num.rfind("(")
    end=num.find(")")
    num=num[:start]+solve(num[start:end+1])+num[end+1:]
print("Final crunch",num)
count=0
for i in num[:num.find("/")]:
    count+=int(i)
print("Final answer",count)