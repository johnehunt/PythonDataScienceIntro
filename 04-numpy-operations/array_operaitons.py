import numpy as np

# Sort an array
arr = np.array([1, 6, 2, 9, 4, 5])
print(f'unsorted array: {arr}')
arr.sort()
print(f'sorted array: {arr}')

# find unique values
arr = np.array([1, 6, 1, 2, 6, 6, 2])
print(f'original array: {arr}')
arr2 = np.unique(arr)
print(f'Unique values: {arr2}')

# Look for membership
arr3 = np.in1d(arr, [1, 2])
print(arr3)

# Handle boolean values
arr = np.array([True, False, False, True, False])
print(f'Boolean array: {arr}')
print(f'arr.any(): {arr.any()}')
print(f'any.all(): {arr.all()}')
