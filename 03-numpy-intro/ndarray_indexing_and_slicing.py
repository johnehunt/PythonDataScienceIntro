import numpy as np

arr1 = np.array([1, 2, 3, 4])
print(f'arr1: {arr1}')

print(f'arr1[1]: {arr1[1]}')
print(f'arr1[1:3]: {arr1[1:3]}')

arr2 = arr1[1:3]
print(f'arr2: {arr2}')

arr1[1:3] = -1
print(f'modified arr1: {arr1}')

arr2[1] = 100
print(f'arr2: {arr2}')
print(f'final arr1: {arr1}')

print('-' * 25)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'arr2d: {arr2d}')

print(f'arr2d[1]: {arr2d[1]}')
# exactly the same
print(f'arr2d[1][0]: {arr2d[1][0]}')
print(f'arr2d[1, 0]: {arr2d[1, 0]}')
# Can also slice higher dim arrays
print(f'arr2d[0:2]: {arr2d[0:2]}')

print('-' * 25)
print(f'arr2d[:2, 1:] \n{arr2d[:2, 1:]}')

print(f'arr2d[1:2, :2] \n{arr2d[1:2, :2]}')

print(f'arr2d[2, 1:2] \n{arr2d[2, 1:2]}')



