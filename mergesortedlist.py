l1=[];
l2=[];
n=int(input("enter size of list-1 : "));
n1=int(input("enter size of list-2 : "));
print("enter list-1: ");
for i in range(n):
    l1.append(input());
print("enter list-2 :")
for i in range(n1):
    l2.append(input());
l1.sort();
l2.sort();

l=list(l1+l2);
l.sort()
print(l);