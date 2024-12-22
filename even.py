n=int(input("Enter the number:"))
if n ==2 :
    print("this is even number")
    print("this is prime number")
elif n%2==0:
    print("This is even number")
else:
    print("This is odd number")   
for i in range(2,(n//2)+1):
        if (n%i)==0:
            print(n,"not prime number")
        elif n==9:
             print("not a prime nu")
        else:
            print(n," a prime number")
