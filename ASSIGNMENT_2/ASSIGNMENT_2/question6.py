''' Write a program that prompts the user for a series of integers and stores in a list only the values between 1-100, and displays the resulting list.'''
def filter_numbers():
    numbers = []
    while True:
        num = input("Enter an integer (or 'q' to quit): ")
        if num.lower() == 'q':
            break
        if num.isdigit() and 1 <= int(num) <= 100:
            numbers.append(int(num))
    print("Filtered numbers:", numbers)

filter_numbers()
