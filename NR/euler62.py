#https://projecteuler.net/problem=62
def permutation(num1, num2):
    num1=digitlist(num1)
    num2=digitlist(num2)
    if(len(num1)!=len(num2)):
        return False
    for dig in num1:
        if(dig not in num2):
            return False
        num2.remove(dig)
    return True
def digitlist(num):
    l=[]
    num=str(num)
    for digit in num:
        l.append(int(digit))
    return l
cubes=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
base=0
cube=0
leng=1
while(leng<15):
    cubes[leng].append(cube)
    base+=1
    cube=base**3
    leng=len(str(cube))
for l in range(1, 15):
    lis=cubes[l]
    for a in range(len(lis)):
        perms=[lis[a]]
        for b in range(a+1, len(lis)):
            if(permutation(lis[a], lis[b])):
                perms.append(lis[b])
        if(len(perms)>4):
            print(lis)
            input(str(perms)+" are cube permutations of one another")
    print("Reached",l)