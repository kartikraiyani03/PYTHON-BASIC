def high(a,b,c):
    if(a>b):
        if(a>c):
            print("\n",a,"is Bigger")
        else:
            print("\n",c,"is Bigger")
    else:
        if(b>c):
            print("\n",b,"is Bigger")
        else:
            print("\n",c,"is Bigger")
            
a = int(input("Enter the First Number : \n"))
b = int(input("Enter the Second Number : \n"))
c = int(input("Enter the Third Number : \n"))

high(a,b,c)