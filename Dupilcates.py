l=[];
n=int(input("enter size of list"));
for i in range(n):
    l.append(input());
l=set(l);
l=list(l);
print(l);