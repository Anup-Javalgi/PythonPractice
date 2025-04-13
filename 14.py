# Python calculator

num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))
operator = input("Enter an opereator(+, -, *, %, **, /, //): ")

if(operator == '+'):
    print(f"{num1} {operator} {num2} = ", num1+num2)
elif(operator == '-'):
    print(f"{num1} {operator} {num2} = ", num1-num2)
elif(operator == '*'):
    print(f"{num1} {operator} {num2} = ", num1*num2)
elif(operator == '/'):
    print(f"{num1} {operator} {num2} = ", num1/num2)
elif(operator == '%'):
    print(f"{num1} {operator} {num2} = ", num1%num2)
elif(operator == '**'):
    print(f"{num1} {operator} {num2} = ", num1**num2)
elif(operator == '//'):
    print(f"{num1} {operator} {num2} = ", num1//num2)
else:
    print("Operator not valid!!!")
    