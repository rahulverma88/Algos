import numpy as np
import math

num_sims = 1000000
n_successes = 0

for i in range(1,num_sims):
    samples = np.zeros(23)
    for j in range(23):
        bday_cur = 1 + math.floor(365 * np.random.random())
        if (bday_cur in samples):
            n_successes += 1
            break
        else:
            samples[j] = bday_cur


print('Probability of two people having same bday:', n_successes/num_sims)