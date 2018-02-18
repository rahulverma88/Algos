import math

largest = 1

def is_palindrome(num_str):
    nchar = len(num_str)

    check = 0
    cur = False
    while cur < nchar/2:
        if num_str[cur] != num_str[nchar-cur-1]:
            check = False
            break
        else:
            check = True
            cur += 1

    return check

for i in range(100,999):
    for j in range(100,999):
        prod = i*j
        prod_str = str(prod)
        if (is_palindrome(prod_str)):
            if (prod > largest):
                largest = prod

print(largest)