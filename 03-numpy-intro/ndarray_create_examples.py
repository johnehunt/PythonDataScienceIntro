import numpy as np

array1d = np.array([1, 2, 3, 4, 5])
print(array1d)

array2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(array2d)

array3 = np.array([1, 2, 3.0])
print(array3)

print('-' * 25)

arr1 = np.zeros(5)
print(arr1)

arr2 = np.ones(5)
print(arr2)

arr3 = np.empty((2, 3, 2))
print(arr3)

arr4 = np.arange(5)
print(arr4)

arr5 = np.identity(4)
print(arr5)

arr6 = np.full(4, 2)
print(arr6)
