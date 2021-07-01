import numpy as np

##
## unary ufuncs
##

arr = np.array([0, 1, 2, 3,4, 5, 6, 7, 7])
# obtain the square root of each value in array
print(np.sqrt(arr))

# obtain the exponential of each element in the array
print(np.exp(arr))

# Get the flow of a set of values
arr = np.array([1.3, 4.5, 6.4, 3.2])
print(np.floor(arr))

##
## Binary ufuncs
##

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([2, 4, 6, 8])

# Add two arrays together
print(np.maximum(arr1, arr2))

# add two arrays
print(np.add(arr1, arr2))

# Compare two arrays
print(np.less(arr1, arr2))

