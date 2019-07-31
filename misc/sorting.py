def radix1(list):
    buckets=[]
    maxvalue=list[0]
    minvalue=list[0]
    for i in range(len(list)):
        if list[i]>maxvalue:
            maxvalue=list[i]
        if list[i]<minvalue:
            minvalue=list[i]
    for i in range(minvalue-1, maxvalue+1):
        buckets.append([])
    for i in range(len(list)):
        buckets[list[i]-minvalue].append(list[i])
    newlist=[]
    for i in range(len(buckets)):
        newlist=newlist+buckets[i]
    return newlist
def radix2(list):
    buckets=[]
    maxvalue=list[0]
    minvalue=list[0]
    for i in range(len(list)):
        if list[i]>maxvalue:
            maxvalue=list[i]
        if list[i]<minvalue:
            minvalue=list[i]
    for i in range(minvalue, maxvalue+1):
        if(i in list and [i] not in buckets):
            buckets.append([i])
    for i in range(len(list)):
        for j in range(len(buckets)):
            if(buckets[j][0]==list[i]):
                buckets[j].append(list[i])
    newlist=[]
    for i in range(len(buckets)):
        newlist=newlist+buckets[i][1:]
    return newlist
def quicksort(list):
    if(len(list)<2):
        return list
    pivotspot=len(list)-1
    pivot=list[pivotspot]
    i=0
    while i<pivotspot:
        if(list[i]>=pivot):
            list.append(list.pop(i))
            i-=1
            pivotspot-=1
        i+=1
    return quicksort(list[:pivotspot])+[list[pivotspot]]+quicksort(list[pivotspot+1:])
def mergesort(list):
    if(len(list)==1):
        return(list)
    return merge(mergesort(list[(int(len(list)/2)):]),mergesort(list[:(int(len(list)/2))]))
def merge(list1, list2):
    newlist=[]
    while(len(list1)>0 and len(list2)>0):
        if(list1[0]<list2[0]):
            newlist.append(list1.pop(0))
        else:
            newlist.append(list2.pop(0))
    return newlist+list1+list2#why do i add list1 and list2 here
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
print(l)#sort of choosing
