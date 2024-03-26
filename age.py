age=int(input("enter the age"))
isAdult=True if age>=18 else False
if isAdult:
	print("you are adult")
else:
	print("you are minor")