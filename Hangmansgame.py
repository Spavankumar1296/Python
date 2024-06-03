str1=input("Enter any word:");
str2=[]
user=input("enter user name")
for i in range(len(str1)):
    str2.append("_")
print(str2)
count=len(str1)
# unnder="_"
while count!= -1 and "_" in str2:
    guess=input("Enter any word:")
    if guess in str1 and "_" in str2:
        for  i in range(len(str1)):
            if str1[i]==guess:
                str2[i]=guess
                print(str2)            
    else:
        print("you are not correct you have " ,count, "chances")
        count =count-1
if "_" not in str2:
        print(user,",you win")
else:
    print(user,",you loose")
