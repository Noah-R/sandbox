def romanToNumber(roman):
    digits=[]
    total=0
    for index in range(len(roman)):
        if(roman[index]=="I"):
            digits.append(1)
        if(roman[index]=="V"):
            digits.append(5)
        if(roman[index]=="X"):
            digits.append(10)
        if(roman[index]=="L"):
            digits.append(50)
        if(roman[index]=="C"):
            digits.append(100)
        if(roman[index]=="D"):
            digits.append(500)
        if(roman[index]=="M"):
            digits.append(1000)
    for index in range(len(digits)):
        if(index<len(digits)-1 and digits[index+1]>digits[index]):
            total-=digits[index]
        else:
            total+=digits[index]
    return total

def numberToRoman(number):
    roman=""
    while(number>0):
        if(number>=1000):
            roman+="M"
            number-=1000
        elif(number>=900):
            roman+="CM"
            number-=900
        elif(number>=500):
            roman+="D"
            number-=500
        elif(number>=400):
            roman+="CD"
            number-=400
        elif(number>=100):
            roman+="C"
            number-=100
        elif(number>=90):
            roman+="XC"
            number-=90
        elif(number>=50):
            roman+="L"
            number-=50
        elif(number>=40):
            roman+="XL"
            number-=40
        elif(number>=10):
            roman+="X"
            number-=10
        elif(number>=9):
            roman+="IX"
            number-=9
        elif(number>=5):
            roman+="V"
            number-=5
        elif(number>=4):
            roman+="IV"
            number-=4
        elif(number>=1):
            roman+="I"
            number-=1
    return roman

answer=0
f=open("roman.txt", "r")#insert your absolute filepath here
for line in f:
    longer=line.replace("\n","")
    print(longer)
    shorter=numberToRoman(romanToNumber(longer))
    answer+=len(longer)-len(shorter)
print("Final answer: "+str(answer))
#might want to close the file stream