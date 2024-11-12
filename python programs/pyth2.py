n=int(input("enter a number to check whether it is prime or not:"))
if n<=1:
    print(f"{n} is not a prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number")
            break
        else:
            print(n,"is a prime number")
            break