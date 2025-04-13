'''Create a 5x5 matrix with row values ranging from 0 to 4'''

import numpy as np

matrix = np.tile(np.arange(5), (5, 1))

print(matrix)
