import numpy as np

nums = np.linspace(1,100,100)

nums_sq = np.square(nums)
sum_sq = sum(nums_sq)
sum_sq_sq = np.square(sum(nums))

print(sum_sq_sq-sum_sq)