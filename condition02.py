a = input("Enter the First Number : ")
b = input("Enter the Second Number : ")
c = input("Enter the Third Number : ")
d = input("Enter the Fourth Number : ")

if(a>b and a>b and a>c):
    print("Bigger Number is ",a)
elif(b>a and b>c and b>d):
    print("Bigger Number is ",b)
elif(c>a and c>b and c>d):
    print("Bigger Number is ",c)
else:
    print("Bigger Number is ",d)