import numpy as np

#data = np.array([[131,201,630,537,805],[673,96,803,699,732],[234,342,746,497,524],[103,965,422,121,37],[18,150,111,956,331]])

with open('p081_matrix.txt') as f:
    data = f.read()

data = data.split('\n')
del data[-1]
data = list(map(lambda x: x.split(','),data))
data = np.array([list(map(lambda x: int(x), i)) for i in data])
data = data.T

side = 80

max_steps = 2*(side - 1)

mat = -1*np.ones([side,side])

mat[side - 1, side - 1] = 0

for i in range(side-1,-1,-1):
    for j in range(side-1,-1,-1):
        if mat[i-1,j] == -1:
            mat[i-1,j] = mat[i,j] + 1
        if mat[i,j-1] == -1:
            mat[i,j-1] = mat[i,j] + 1


for i in range(1,max_steps+1):
    indices = ((np.asarray(np.where(mat == i))).T)

    for j in indices:
        if j[0] + 1 == side:
            right = 1e10
        else:
            right = data[j[0]+1,j[1]]

        if j[1] + 1 == side:
            bot = 1e10
        else:
            bot = data[j[0],j[1]+1]

        data[j[0],j[1]] += min(right,bot)

print(data[0,0])

