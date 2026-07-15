num1=float(input("Enter a number: "))
num2=float(input("Enter other number: "))
op=input("Enter operation to perform: ")
result=0.0
if op=='+':
    result=num1+num2
    print(result)
elif op=='-':
    result=num1-num2
    print(result)
elif op=='*':
    result=num1*num2
    print(result)
elif op=='/':
    if num2!=0:
        result=num1/num2
        print(result)
    else:
        print('ZeroDivisionError')
else:
    print("Invalid Operator")
