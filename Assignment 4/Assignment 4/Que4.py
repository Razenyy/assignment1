'''Can you create a identity matrix of shape (3,4). If yes write code for it'''

import numpy as np


identity_matrix = np.eye(3)

print(identity_matrix)

import numpy as np


matrix = np.zeros((3, 4))
for i in range(min(matrix.shape)):
    matrix[i, i] = 1

print(matrix)
