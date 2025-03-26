'''Write a Python program that accepts a string and calculates the number of digits and letters'''
def count_digits_and_letters(s):
    num_digits = sum(c.isdigit() for c in s)
    num_letters = sum(c.isalpha() for c in s)
    return num_digits, num_letters


user_input = input("Enter a string: ")

digits, letters = count_digits_and_letters(user_input)

print(f"Number of letters: {letters}")
print(f"Number of digits: {digits}")