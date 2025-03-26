''' Write a program that prompts the user for two integer values and displays the results of the first number divided by the second, with exactly two decimal places displayed.'''
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
if num2 != 0:
    division_result = num1 / num2
    print(f"2. Result of division: {division_result:.2f}")
else:
    print("2. Division by zero is not allowed.")