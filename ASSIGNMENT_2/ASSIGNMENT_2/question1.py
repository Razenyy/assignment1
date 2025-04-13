'''Write a function that accepts a string and calculate the number of upper case letters and lower case letters'''
def count_case_letters(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())

    return upper_count, lower_count
string = "Happy Birthday"
upper, lower = count_case_letters(string)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
