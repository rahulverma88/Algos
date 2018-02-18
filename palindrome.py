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

print(is_palindrome('12345'))
print(is_palindrome('12321'))
print(is_palindrome('783387'))
print(is_palindrome('98789'))