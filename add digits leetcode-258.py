def addDigits(num:int):
    while num>9:
        temp=0
        while num>0:
            temp+=num%10
            num=num//10
        num=temp
    return num
num=int(input())
print(addDigits(num))
