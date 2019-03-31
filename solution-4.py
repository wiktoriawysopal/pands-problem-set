n = int(input("Please enter a positive integer ")) #user enter a positive integer
while n != 1: # check for loop to infinity
    if n % 2 == 0: #if the number is even
        n = n/2
        print(n) 
    else: #if the number is odd
        n = (n * 3) + 1
        print(n)
