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
    num=eval(s)
    return str(int(num))
for i in range(1,100):
    #take last number, put in parentheses and add 1/sequence[i]
    x=findlastnum(num)
    start=x[0]
    end=x[1]
    num=num[:start]+"("+num[start:end+1]+"+1/"+str(sequence[i])+")"+num[end+1:]
num=num[1:len(num)-1]
while("(" in num):
    start=num.rfind("(")
    end=num.find(")")
    num=num[:start]+solve(num[start:end+1])+num[end+1:]
print(num)
#(2+1/(1+1/(2+1/(1+1/(1+1/(4+1/(1+1/(1+1/(6+1/(1+1/(1+1/(8+1/(1+1/(1+1/(10+1/(1+1/(1+1/(12+1/(1+1/(1+1/(14+1/(1+1/(1+1/(16+1/(1+1/(1+1/(18+1/(1+1/(1+1/(20+1/(1+1/(1+1/(22+1/(1+1/(1+1/(24+1/(1+1/(1+1/(26+1/(1+1/(1+1/(28+1/(1+1/(1+1/(30+1/(1+1/(1+1/(32+1/(1+1/(1+1/(34+1/(1+1/(1+1/(36+1/(1+1/(1+1/(38+1/(1+1/(1+1/(40+1/(1+1/(1+1/(42+1/(1+1/(1+1/(44+1/(1+1/(1+1/(46+1/(1+1/(1+1/(48+1/(1+1/(1+1/(50+1/(1+1/(1+1/(52+1/(1+1/(1+1/(54+1/(1+1/(1+1/(56+1/(1+1/(1+1/(58+1/(1+1/(1+1/(60+1/(1+1/(1+1/(62+1/(1+1/(1+1/(64+1/(1+1/(1+1/(66+1/1)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))