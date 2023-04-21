# Factorial Using Recusrion

def facto(n):
    if(n==0 or n ==1):
        return 1
    else:
        return n*facto(n-1)
    
    
n = int(input("Enter the Number : \n"))
print("The Factorial is",facto(n))

# Factorial Using Itration

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    return fact
        
n = int(input("Enter the Number : \n"))

print(factorial(n))


