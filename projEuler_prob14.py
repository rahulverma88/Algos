start_num = 1
longest = 1

while start_num < 1e6:
    next_num = start_num
    cur_longest = 1
    while next_num > 1:
        if next_num % 2 == 0:
            next_num = next_num/2
        else:
            next_num = 3*next_num + 1
        cur_longest += 1

    if cur_longest > longest:
        longest = cur_longest
        answer = start_num

    start_num += 1

print(answer)
