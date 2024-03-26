string1=input("enter the string ")
string2=list(string1)
for i in range(len(string2)):
    if string2[i]=='o':
        print(f"charcter 'o' is fount at index {i}")
        break
    else:
        print("letter 'o' is not found")