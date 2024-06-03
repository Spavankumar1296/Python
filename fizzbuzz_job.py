n=int(input("enter the number: "))
for i in range(n):
    if(i%3==0 and i%5==0):
        print("fuzzBuzz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0):
        print("fizz")
    else:
        print(i)
  