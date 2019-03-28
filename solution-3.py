for i in range(1000,10000): # i represent range between 1,000 and 10,000
    if (i % 6 == 0) and not(i % 12 == 0): #if statments, with two conditions one is positive and the other is negative, which means that the number is divisible by first condition but not by the second one. Thats why I included "not" before rounded brackets.
        print(i) #the if statment returns all the values divisible by 6, but not 12.

