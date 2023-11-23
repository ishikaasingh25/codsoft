a=float(input("enter the first number\n"))
b=float(input("enter the second number\n"))

def add(a, b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def divide(a,b):
    print(a/b)
ch=int(input("Enter the operation :\n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division\n"))

if ch==1:
    add(a,b)
elif ch==2:
    subtract(a,b)
elif ch==3:
    multiply(a,b)
elif ch==4:
    divide(a,b)
else:
    print("invalid choice of operation")



