print("marksheet")
a=int(input("enter your j2ee mark"))
b=int(input("enter your python mark"))
c=int(input("enter your java mark"))
d=int(input("enter your javascript mark"))
e=int(input("enter your oracle mark"))
total=(a+b+c+d+e)
print("your total mark:",total)
per=(total/500)*100
print("your precentage %",per)
if(per>=90 and per<100):
    print("your grade is A")
elif(per>=80 and per<90):
    print("your grade is B")
elif(per>=70 and per<80):
    print("your grade is c")
elif(per>=60 and per<70):
    print("your grade is d")
elif(per>=40 and per<60):
    print("your grade is e")
else:
    print("your are fail")
    
    
