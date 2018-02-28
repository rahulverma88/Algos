import primes
import numpy as np

range_a = range(-999,1000)
range_b = range(-1000,1001)

max_num_primes = 0

for a in range_a:
    for b in range_b:
        cur_max_num = 0
        n = 0
        while primes.isprime(n*n + a*n + b):
                cur_max_num += 1
                n += 1

        if cur_max_num > max_num_primes:
            max_num_primes = cur_max_num
            max_prod = a*b
            a_max = a
            b_max = b


print(max_num_primes)
print(a_max,b_max)
print(a_max*b_max)

