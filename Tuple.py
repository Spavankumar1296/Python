t=(10,20,30,40,10,10,20,50)
print(len(t))
print(max(t))
print(min(t))
print(t.count(10))
print(t.count(20))
print(t.index(20))
print(t.index(10))
print(sorted(t))
print(type(t))
print(tuple(range(10)))
t=(1,2,3,4,5,6)
print("Tuple :",t)
print("First elements of Tuple:",t[0])
print("Sliced tuple :",t[2:4])
for i in t:
    print(i)
t1=(1,2,3,4,5,6,7,8)
t2=(9,10,11,12,13,14,15,16)
con= t1+t2
print("concatenation of tuple : ",con)
print("length :",len(con))
