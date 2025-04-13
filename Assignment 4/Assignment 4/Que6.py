'''Write a program to input an array of numbers from the user (at least 10 elements in list), sort them and perform slicing operations to get elements between indexes such as 2-5, 5-8, 2-9'''


numbers = list(map(int, input("Enter at least 10 numbers separated by spaces: ").split()))

if len(numbers) < 10:
    print("Please enter at least 10 numbers.")
else:
    
    numbers.sort()
    print("\nSorted array:", numbers)

    print("\nSlicing operations:")
    print("Elements from index 2 to 5:", numbers[2:6])  # Slicing from index 2 to 5
    print("Elements from index 5 to 8:", numbers[5:9])  # Slicing from index 5 to 8
    print("Elements from index 2 to 9:", numbers[2:10])  # Slicing from index 2 to 9
