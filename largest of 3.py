a=input()
x,y,z=a.split(",")
num1=int(x)
num2=int(y)
num3=int(z)
great=0
if num1>num2:
    if num1>num3:
        great=num1
    else:
        grear=num3
if num2>num1:
    if num2>num3:
        great=num2
    else:
        grear=num3
if num3>num1:
    if num3>num2:
        great=num3
    else:
        grear=num2
print(great)
        

        
