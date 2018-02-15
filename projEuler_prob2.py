import numpy as np
import math

num_1 = 1
num_2 = 2
sum = num_2
fib_limit = 4000000
next_num = 0

while next_num < fib_limit:
    next_num = num_1 + num_2
    if (next_num % 2 == 0):
        sum += next_num
    num_1 = num_2
    num_2 = next_num

print(sum)