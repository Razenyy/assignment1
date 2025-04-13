'''Write a Pandas program to add, subtract, multiple and divide two Pandas Series'''

import pandas as pd


series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([5, 15, 25, 35, 45])


addition = series1 + series2

subtraction = series1 - series2

multiplication = series1 * series2


division = series1 / series2


print("Series 1:")
print(series1)

print("\nSeries 2:")
print(series2)

print("\nAddition of Series 1 and Series 2:")
print(addition)

print("\nSubtraction of Series 1 and Series 2:")
print(subtraction)

print("\nMultiplication of Series 1 and Series 2:")
print(multiplication)

print("\nDivision of Series 1 and Series 2:")
print(division)
