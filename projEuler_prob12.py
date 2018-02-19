import primes
import numpy as np

def get_num_div(cur_num):
    num_div = 1
    factors = []
    for i in range(2, int(np.floor(np.sqrt(cur_num)))):
        if primes.isprime(i):
            factors.append(i)

    powers = []

    ind = 0
    for i in factors:
        j = cur_num
        powers.append(0)
        cur_power = 0
        while j % i == 0:
            j = j / i
            cur_power += 1
        powers[ind] = cur_power
        ind += 1

    for i in powers:
        num_div *= (i + 1)

    return num_div

i = 3
num_div = 1


while num_div <= 500:
    i += 1
    cur_num = i*(i+1)/2
    num_div = get_num_div(cur_num)

print(cur_num)

