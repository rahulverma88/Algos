import primes

i = 3
sum = 2

while i < 2e6:
    if (primes.isprime(i)):
        sum += i
    i += 2

print(sum)

