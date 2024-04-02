def linear(lst,key):
    for i in range(len(lst)):
        if lst[i]==key:
            return i
        else:
            return -1
lst=[]
n=int(input("Enter the list size: "))
for i in range(n):
    lst.append(int(input()))
key=int(input("Enter the key value "))
index=linear(lst,key)
if index!= -1:
    print(f"element is found at {index}")
else:
    print("Element is not found")