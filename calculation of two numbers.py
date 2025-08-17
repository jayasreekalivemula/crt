num1=int(input("Give 1st Number: "))
num2=int(input("Give 2st Number: "))
Operator=input("Give an Operator: ")
if Operator == "+":
    print(f"Addition of Two Numbers is {num1+num2}")
elif Operator == "-":
    print(f"Subtraction of Two Numbers is {num1-num2}")
elif Operator == "*":
    print(f"Multiplication of Two Numbers is {num1*num2}")
elif Operator == "/":
    print(f"Division of Two Numbers is {num1/num2}")
else:
    print("Invalid Operator")
    
    
