def worth(c):
    val = ord(c.lower()) - 96
    return val


with open('p022_names.txt') as f:
    file_data = f.read()

names_list = file_data.split(',')
names_list = list(map(lambda x: x.replace('"',''), names_list))
names_list.sort()

ind = 1
tot_score = 0

for i in names_list:
    char_list = list(i)
    val = 0
    for j in char_list:
        val += worth(j)
    tot_score += val * ind
    ind += 1


print(tot_score)
