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

i = 13
w = 2
ind = 6

while ind < 10001:
    i += 1
    if isprime(i):
        ind += 1

print(i)
print(isprime(i))