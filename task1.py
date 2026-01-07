a=int(input("Enter the first number: "))
b=int(input("Enter the second  number: "))
addition=a+b
subtraction=a-b
multiplication=a*b
print("Addition:",addition)
print("Subtraction:",subtraction)
print("Multiplication:",multiplication)
if b==0:
    print("Division by zero is not allowed.")
else:
    print("Division:",a/b)