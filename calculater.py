print("calclulator")
print("1=addition")
print("2=substraction")
print("3=multiplication")
print("4=division")
choice=(input("enter choice number 1-2-3-4: "))
x=float(input("enter the first number: "))
y=float(input("enter the second number: "))
def calc(choice):
    if(choice=='1'):
        print(x+y)
    elif(choice=='2'):
        print(x-y)
    elif(choice=='3'):
        print(x*y)
    elif(choice=='4'):
        print(x/y)
    else:
        print(" choice only 1 to 4 ")
calc(choice)
