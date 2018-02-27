from itertools import permutations

nums = list(range(10))

num_perms = list(set(permutations(nums)))
num_perms = list(map(lambda x: list(x),num_perms))
num_perms = list(map(lambda x: ''.join(str(y) for y in x), num_perms))
num_perms.sort()
num_perms = list(map(lambda x: int(x), num_perms))

ind = 1000000 - 1
print(num_perms[ind])