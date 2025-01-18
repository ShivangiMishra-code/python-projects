#making calculator
print("enter the first number")
a=int(input())
print("enter the second number")
b=int(input())
print("entrer the operator")
c=input()
if(c=="+"):
  print("The sum is ",a+b)
elif(c=="-"):
    print("The difference is ",a-b)
elif(c=="*"):
    print("The product is ",a*b)
elif (c == "/"):
    print("The quotient is ",a/b)
elif(c=="**"):
    print("The power is ",a**b)
elif(c=="%"):
    print("The remainder is ",a%b)