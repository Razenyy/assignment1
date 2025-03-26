''' Write a program to find the Euclidean distance between two coordinates. Take both the coordinates from the user as input'''
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)*2 + (y2 - y1)*2)

x1, y1 = map(float, input("Enter the first coordinate (x1, y1), separated by space: ").split())
x2, y2 = map(float, input("Enter the second coordinate (x2, y2), separated by space: ").split())

distance = euclidean_distance(x1, y1, x2, y2)
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")