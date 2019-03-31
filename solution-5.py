n = int(input("Please enter a positive number ."))
if n>1:
    for i in range(2,n):
        if(n%1) == 0:
            print (n) + "is not a prime number"
            break
    else:
        print (n) + "is a prime number"
else:
    print(n) + "is not a prime number"
    