n = int(input("Enter the Number : \n"))
c=0

for i in range(2,n):
    if(n % i == 0):
        c=c+1

if(c==2):
    print("Number is Not Prime")
else:
    print("Number is Prime")
     