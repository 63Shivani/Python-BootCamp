age1 = int(input("enter age\n"))
age2 = int(input("enter age\n"))
age3 = int(input("enter age\n"))
age4 = int(input("enter age\n"))
if(age1>age2 and age1>age3 and age1>age4):
    print(age1,"year old is oldest")
elif(age2>age1 and age2>age3 and age2>age4):
    print(age2,"year old is oldest")
elif(age3>age1 and age3>age2 and age3>age4):
    print(age3,"year old is oldest")
else:
    print(age4,"year old is oldest")
