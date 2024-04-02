num1=int(input("enter the number-1"))
num2=int(input("enter the number-2"))
add=num1+num2
sub=num1-num2
mult=num1*num2
exp=num1**num2
print("Addition :",add)
print("Subtraction:",sub)
print("multiplication :", mult)
print("Exponentiation:",exp)
if num2!=0:
    div=num1/num2
    floor_div=num1//num2
    mod=num1%num2
    print("Division:",div)
    print("Floor_Division:",floor_div)
    print("Modulus:",mod)
else:
    print("Denominator not negative")
