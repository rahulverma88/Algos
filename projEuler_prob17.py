import inflect

p = inflect.engine()

num_letters = 0

for i in range(1,1001):
    cur_num = p.number_to_words(i).replace(' ','').replace('-','')
    num_letters += len(cur_num)

print(num_letters)