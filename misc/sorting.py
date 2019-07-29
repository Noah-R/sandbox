def insertionsort(l):
    l2=[]
    while(len(l)>0):
      insert(l.pop(0), l2)
    l=l2
    return l
def insert(num, l):
  for i in range(len(l)):
    if(l[i]>num):
      l.insert(i, num)
      return
  l.append(num)
  return
def bubblesort(l):
    for a in range(len(l)):
        for b in range(len(l)):
            if l[a]<l[b]:
                temp=l[a]
                l[a]=l[b]
                l[b]=temp
    return l
from random import randint
l=[]
num=int(input("number of items"))
for i in range(num):
    l.append(randint(1, 1000))
print(l)
print(bubblesort(l))
#todo: integrate code from chromeos downloads folder text files
