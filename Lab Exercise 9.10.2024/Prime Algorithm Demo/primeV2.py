#Prime number checker version 2
#Author: nmessa
#Date: 9/9/2024

import time, math

#number = 999983
number = 99999989
start_time = time.time()

#test for prime
for i in range(2, int(math.sqrt(number)+1)):
    if number%i == 0:
        print("Not prime")
        break
else:
    print("The number is prime")
end_time = time.time()
execution_time = end_time - start_time
print("Execution time =",execution_time, "seconds")
