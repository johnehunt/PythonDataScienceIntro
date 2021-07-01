import numpy as np

arr1 = np.array([[1, 2], [4, 5]])
arr2 = np.array([[2, 6], [2, 3]])

print(f'arr1 * arr2: \n{arr1 * arr2}')
print(f'arr1.dot(arr2): \n{arr1.dot(arr2)}')

arr3 = np.array([[1, 2, 3], [2, 3, 4]])
arr4 = np.array([2, 3, 5])
print(f'arr3.dot(arr4): \n{arr3.dot(arr4)}')

print('-' * 25)

from numpy.linalg import inv, qr, solve, det
from numpy import trace, diag

arr1 = np.array([[1, 2], [4, 5]])
print(f'inv(arr1): \n{inv(arr1)}')

print(f'qr(arr1): \n{qr(arr1)}')

print(f'diag(arr1): {diag(arr1)}')
print(f'trace(arr1): {trace(arr1)}')
print(f'det(arr1): {det(arr1)}')

a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
x = solve(a, b)
print(x)



