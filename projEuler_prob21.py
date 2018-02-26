import primes
import numpy as np

def make_prime_list(n):
    prime_list = []
    for i in range(2,n+1):
        if primes.isprime(i):
            prime_list.append(i)

    return prime_list


def get_factors_simple(n):
    factors = set()
    for i in range(2,int(np.sqrt(n)+2)):
        if n % i == 0:
            factors.add(i)
            factors.add(int(n/i))

    factors = list(factors)
    factors.append(1)
    return factors


a = 2
sum_amicable = 0
amicable_nums = set()

while a < 10000:
    b = np.sum(get_factors_simple(a))

    if a == np.sum(get_factors_simple(b)) and a != b and b < 10000:
        amicable_nums.update((a,b))

    a += 1

print(np.sum(list(amicable_nums)))
print(amicable_nums)
