def sum(a,b):
    sum=a+b
    print(sum)
def subtraction(a,b):
    sub=a-b
    print(sub)
def multiplication(a,b):
    mul=a*b
    print(mul)
def division(a,b):
    div=a/b
    print(div)

print('1:Sum\n 2:Subtraction\n 3:Multiplication\n 4:Division')
choice=int(input('Select your choice :'))
while choice<=4:
    a=int(input("Enter the first number :"))
    b=int(input("Enter the second number :"))
    if choice==1:
        sum(a,b)
    elif choice==2:
        subtraction(a,b)
    elif choice==3:
        multiplication(a,b)
    elif choice==4:
        division(a,b)
    else:
        break