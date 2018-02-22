
with open('p067_triangle.txt') as f:
    read_data = f.read()

tri_rows = read_data.split('\n')

del(tri_rows[-1])

num_rows = len(tri_rows)


for i in range(num_rows):
    tri_rows[i] = list(map(lambda x: int(x), tri_rows[i].split(' ')))

i = num_rows - 1

while i >= 0:
    cur_row = tri_rows[i]

    for j in range(len(cur_row)-1):
        if cur_row[j] > cur_row[j+1]:
            tri_rows[i-1][j] += cur_row[j]
        else:
            tri_rows[i-1][j] += cur_row[j+1]

    i -= 1

print(tri_rows[0])