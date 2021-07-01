import numpy as np

names = np.array(['Adam', 'Phoebe', 'Jasmine', 'Gryff', 'Jasmine', 'Adam', 'Adam'])

exam_results = np.array([
        [56, 65, 72],
        [67, 65, 85],
        [62, 78, 55],
        [56, 67, 65],
        [67, 78, 89],
        [87, 56, 45],
        [56, 87, 98]
])

print(f'names: {names}')
print(f'exam_results: {exam_results}')

# Find all entries for 'Adam' in names
print(f"names == 'Adam' {names == 'Adam'}")

# Find all values that do not equal Adam
print(f"names != 'Adam' {names != 'Adam'}")

mask = [True, False, False, False, False, True, True]
adam_results = exam_results[names == 'Adam']
print(f'adam_results (from mask): {adam_results}')

# Find all marks for Adam
adam_results = exam_results[names == 'Adam']
print(f'adam_results (from ==): {adam_results}')

# Can capture values in a column associated with booleans
adam_results = exam_results[names == 'Adam', 1]
print(f'adam_results for col 1: {adam_results}')

# Select elements where data is below 70
print(f'exam_results[exam_results >= 70]: {exam_results[exam_results >= 70]}')

# Assign values for over 70
exam_results[exam_results >= 70] = 100
print(exam_results)
