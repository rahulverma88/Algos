import numpy as np

size = 20

grid = np.zeros((size+1,size+1))

num_routes = 1

for i in range(size):
    num_routes *= (2*size) - i
    num_routes /= (i) + 1

print(num_routes)