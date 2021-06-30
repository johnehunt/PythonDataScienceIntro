import numpy as np

value1 = np.random.randint(0, 10)
print(f'value1: {value1}')

value2 = np.random.rand(4)
print(f'value2: {value2}')

data1 = np.random.normal(0, 0.1, size=(4, 4))
print(data1)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'list1: {list1}')
data2 = np.random.permutation(list1)
print(f'data2: {data2}')
np.random.shuffle(list1) # in place
print(f'list1: {list1}')

# Can change the seed
np.random.seed(1234)
