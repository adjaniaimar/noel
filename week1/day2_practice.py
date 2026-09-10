import numpy as np

# 1
v1 = np.array([1, 2, 3, 4, 5])
v2 = np.array([10, 20, 30, 40, 50])
print(np.dot(v1, v2))

# 2
matrixx = np.array([[100, 150, 200], 
                    [300, 350, 400], 
                    [500, 550, 600]]
)

print(matrixx.max(axis=0))
print(matrixx.max(axis=1))

print(matrixx.min(axis=0))
print(matrixx.min(axis=1))

print(matrixx.mean(axis=0))
print(matrixx.mean(axis=1))

# 3
temp = np.array([[25, 26, 24],
                 [31, 35, 37],
                 [21, 42, 45],
                 [27, 28, 36],
                 [12, 32, 24],
                 [45, 12, 34],
                 [23, 19, 65],
                 [11, 34, 56],
                 [10, 28, 23],
                 [35, 39, 32]]
)
print(temp.max(axis=0))
print(temp.max(axis=1))

print(temp.min(axis=0))
print(temp.min(axis=1))

normal_temp = (19 - 12) / (42 - 12)
print(normal_temp)

col_min = temp.min(axis=0)
col_max = temp.max(axis=0)
temp_normal = (temp - col_min) / (col_max - col_min)
print(temp_normal)