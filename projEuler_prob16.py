import numpy as np

num_list_str = list(str(pow(2,1000)))
num_list = list(map(lambda x: int(x), num_list_str))

sum = np.sum(num_list)

print(sum)