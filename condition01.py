a = input("Enter the First Number \n")
a = int(a)
b = input("Enter the Second Number \n")
b = int(b)
op = input("Enter the Opration \n")

if(op == '+'):
    result = a+b
    print(result)
elif(op == '-'):
    result = a-b
    print(result)
elif(op == '*'):
    result = a*b
    print(result)
elif(op == '/'):
    result = a/b
    print(result)
else:
    print("Invalid Choice")
   
  
