import numpy as np

def get_factors_simple(n):
    factors = set()
    for i in range(2,int(np.sqrt(n)+2)):
        if n % i == 0:
            factors.add(i)
            factors.add(int(n/i))

    factors = list(factors)
    factors.append(1)
    return factors


def is_abundant(n):
    factor_sum = np.sum(get_factors_simple(n))
    if factor_sum > n:
        return True
    else:
        return False

limit_num = 28123
i = 12
sum_abundant_nums = 0

abundant_nums = set(filter(lambda x: is_abundant(x), range(10,limit_num)))

while i <= limit_num:
    flag = 0
    for j in abundant_nums:
        if i - j in abundant_nums:
            # i can be written as sum of 2 abundant numbers
            sum_abundant_nums += i
            break
    i += 1

total_sum = limit_num*(limit_num+1)/2
sum_non_abundant = total_sum - sum_abundant_nums
print(sum_non_abundant)
