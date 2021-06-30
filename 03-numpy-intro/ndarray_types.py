import numpy as np

array2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(array2d.ndim)
print(array2d.shape)
print(array2d.dtype)

print('-' * 25)

arr1 = np.zeros(5, dtype=np.float64)
print(arr1)

arr2 = np.array([1, 2, 3.0], dtype=np.int32)
print(arr2)

arr3 = arr2.astype(np.float64)
print(arr3)
