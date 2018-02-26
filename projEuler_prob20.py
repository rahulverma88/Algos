import math

n = 100

num = math.factorial(n)
num_str = list(str(num))
num_list = list(map(lambda x:int(x),num_str))

print(sum(num_list))