import math

num = 600851475143
sqrt_num = int(math.sqrt(num))

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


for i in range(2,sqrt_num):
    if (num % i == 0):
        if isprime(i):
            largest_prime = i



print(largest_prime)

