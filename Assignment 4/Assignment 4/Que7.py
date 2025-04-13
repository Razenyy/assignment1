'''Create an array of random integer numbers as a numpy array, sort them and perform operations such as reshaping of the array into matrix of feasible dimensions. (e.g., if we have an array of 1 * 10, then we can reshape it into 2 * 5 or 5 * 2 matrix.) [Hint: Use the array of reshape (row * column)]'''

import numpy as np


random_array = np.random.randint(1, 100, 10)


sorted_array = np.sort(random_array)


reshaped_matrix_2x5 = sorted_array.reshape(2, 5)
reshaped_matrix_5x2 = sorted_array.reshape(5, 2)


print("Sorted Array:")
print(sorted_array)

print("\nReshaped Matrix (2x5):")
print(reshaped_matrix_2x5)

print("\nReshaped Matrix (5x2):")
print(reshaped_matrix_5x2)
