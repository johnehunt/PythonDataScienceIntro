import numpy as np

# Set up some data
arr1 = np.zeros((4, 4), np.int64)
for i in range(4):
    arr1[i] = i

print(arr1)
print()

# Select subset of rows
# in a given order
arr2 = arr1[[1, 3, 0]]
print(arr2)

print('-' * 25)

arr3 = np.arange(16).reshape((4,4))
print(arr3)
print()

# Select values given tuples of indicates
# first list give row and second gives cols
arr4 = arr3[[0, 3, 2], [0, 1, 2]]
print(arr4)

