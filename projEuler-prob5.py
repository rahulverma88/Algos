import math

div = 0

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

factors = []
for i in range(2,21):
    if isprime(i):
        factors.append(i)

powers = []

ind = 0
for i in factors:
    powers.append(0)
    for j in range(2,21):
        cur_power = 0
        while j % i == 0:
            j = j/i
            cur_power += 1
        if cur_power > powers[ind]:
            powers[ind] = cur_power

    ind += 1

print(factors)
print(powers)
print(16*9*5*7*11*13*17*19)