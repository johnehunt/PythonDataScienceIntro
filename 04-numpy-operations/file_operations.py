import numpy as np

arr = np.array([1, 6, 2, 9])
print(f'original data: {arr}')
# Save array to a file
np.save('mydata', arr)

# load data back
arr2 = np.load('mydata.npy')
print(arr2)

# Can save multiple arrays
arr3 = [4, 5, 6, 7]
np.savez('multiple_arrays.npz', a=arr, b= arr3)

# Reload multiple arrays into
# dictionary like structure
data = np.load('multiple_arrays.npz')
print(data)
print(data['a'])
print(data['b'])