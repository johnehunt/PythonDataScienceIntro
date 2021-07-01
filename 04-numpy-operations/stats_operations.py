import numpy as np

arr = np.array([6, 2, 1, 9, 4, 5])
print(f'arr: {arr}')
print(f'arr.sum(): {arr.sum()}')
print(f'arr.min(): {arr.min()}')
print(f'arr.argmin(): {arr.argmin()}')
print(f'arr.cumsum(): {arr.cumsum()}')
print(f'arr.cumprod(): {arr.cumprod()}')

arr = np.array([[6, 2], [1, 9]])
print(arr)
# Produce the sum values across an axis
print(f'arr.sum(axis=1): {arr.sum(axis=1)}')
print(f'arr.sum(axis=0): {arr.sum(axis=0)}')