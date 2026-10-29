a=int(input("Enter frist number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
if (a>=b and a>=c):
    print("The frist number is greatest.",a)
elif (b>=a and b>=c):
    print("The second number is greatest.",b)
else:
    print("The number is smaller.",c)