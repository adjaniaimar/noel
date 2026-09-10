import numpy as np
import time

n = 1_000_000
list_a = list(range(n))
list_b = list(range(n))

# HOW PYTHON WORKS WITHOUT NUMPY
start = time.time()
result = [list_a[i] + list_b[i] for i in range(n)]
print("Python murni:", time.time() - start, "detik")

# WITH NUMPY
arr_a = np.array(list_a)
arr_b = np.array(list_b)

start = time.time()
result_np = arr_a + arr_b
print("NumPy:", time.time() - start, "detik")

# ARRAY
a = np.array([1, 2, 3, 4, 5])
print(a.shape)   # (5,) -> 1 dimensi, 5 elemen
print(a.dtype)   # tipe data

# ARRAY 2D MATRIX
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)  # (2, 3) -> 2 baris, 3 kolom

# VECTOR OPERATIONS
b = np.array([10, 20, 30, 40, 50])
print(a + b)      # [11 22 33 44 55]
print(a * 2)      # [2 4 6 8 10]
print(a ** 2)     # [1 4 9 16 25]

# DOT PRODUCT
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(np.dot(v1, v2))  # 1*4 + 2*5 + 3*6 = 32

# MATRIX MULTIPLICATION
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)  # atau np.matmul(A, B)

# EXAMPLE OF BROADCASTING
a = np.array([1, 2, 3])
print(a + 10)  # [11 12 13] -> 10 di-"broadcast" ke semua elemen

# RELEVANT EXAMPLE: SENSOR DATA
suhu = np.array([
    [25, 26, 24],
    [27, 28, 25],
    [26, 27, 24],
    [28, 29, 26]
])

# SENSOR CALIBRATION: WE WANT TO APPLY A CORRECTION TO EACH SENSOR'S READINGS
koreksi = np.array([-1, 0.5, 0])
suhu_terkoreksi = suhu + koreksi
print(suhu_terkoreksi)