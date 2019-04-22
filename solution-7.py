#The program calculates the approximation of the square root of a positive floating point number
#The number to calculate the square root
n = int(input("Please enter a positive floating point number"))

def newtonSqrt(n):
    estimate = 0.5 * n
    better = 0.5 * (estimate + n/estimate)
    while better != estimate:
        estimate = better
        better = 0.5 * (estimate + n/estimate)
    return = estimate
#Print the result
print(f"The square root of {n} is approx. {estimate})