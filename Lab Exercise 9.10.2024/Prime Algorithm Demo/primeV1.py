#Prime number checker version 1
#Author: nmessa
#Date: 9/9/2024

import time

#number = 999983
number = 99999989
start_time = time.time()

#test for prime
for i in range(2, number):
    if number%i == 0:
        print("Not prime")
        break
else:
    print("The number is prime")
end_time = time.time()
execution_time = end_time - start_time
print("Execution time =",execution_time, "seconds")
