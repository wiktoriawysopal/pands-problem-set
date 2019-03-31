n = int((input)"Please enter any positive number ") #program asks user for a number
if n>1:
    for i in range(2, n): # the range excludes 1 and nth number
        if (n%1) == 0: #if this condition is true 
            print (n) + "is not a prime number."
            break #break come out of the loop
    else: # checks if condition is false for all the iteration
        print (n) + "is a prime number"
else: # this else is aligned with if statement and it checks if a number is greater than 1
    print (n) + "is not a prime number"
