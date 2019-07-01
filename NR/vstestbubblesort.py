from random import randint
l=[]
for i in range(40):
    l.append(randint(1, 1000))
print(l)
for a in range(len(l)):
    for b in range(len(l)):
        if l[a]<l[b]:
            temp=l[a]
            l[a]=l[b]
            l[b]=temp
print(l)