"""
    naive algorith to find prime numbers
    version 1.0
"""

import math
import time

start_time = time.time()
prims = []                   # list of prims
for p in range(2, 500001):   # find prims up to 50000
    prime = True
    for divider in range(2, int(math.sqrt(p))+1):
        if p % divider == 0: # remainder of division is zero
            prime = False    # it is not a prime
    if prime:
        prims.append(p)      # store prime number
print('ready')
print('%d prims in %f seconds' % (len(prims), time.time() - start_time))
