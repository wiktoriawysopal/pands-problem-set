n = int(input("Please enter a positive number ")) #program asks user for a number
if n>1:
    for i in range(2,n): #the range excludes 1 and the nth number
        if(n%1) == 0: #if this condition is true
            print(n, "is not a prime number")
            break #break to come out of the loop
    else: #check if condition is false for all the itereation
        print(n, "is a prime number")
else: #this else is aligned with if statment and it checks if a number is greater than 1
    print (n, "is not a prime number")
