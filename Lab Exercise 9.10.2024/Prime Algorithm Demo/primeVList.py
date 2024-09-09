#Prime number lister
#Author: nmessa
#Date: 9/9/2024

import time, math

#list prime

for number in range(99999900, 100000000):
    isPrime = True
    for i in range(2, int(math.sqrt(number)+1)):
        if number%i == 0:
            isPrime = False
            break
    if isPrime:
        print(number)

