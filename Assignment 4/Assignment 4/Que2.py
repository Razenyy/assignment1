'''Ask user to input two numbers a, b. Write a program to generate a random array of shape (a, b) and print the array and avg of the array'''

import numpy as np


a = int(input("Enter the number of rows (a): "))
b = int(input("Enter the number of columns (b): "))


random_array = np.random.rand(a, b)


print("Generated Random Array:")
print(random_array)

average = np.mean(random_array)


print("Average of the Array:", average)
