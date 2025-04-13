''' Write a program that prompts the user to enter a list of names and store them in a list. The program should display how many times the letter 'a appears within the list.'''
def count_a_in_names():
    names = input("Enter names separated by spaces: ").split()
    count = sum(name.lower().count('a') for name in names)
    print(f"The letter 'a' appears {count} times in the list of names.")

count_a_in_names()
