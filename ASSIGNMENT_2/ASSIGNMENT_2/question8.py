''' Write a program that prompts the user to enter integer values to populate two lists, then prints messages to determine the following: [3]
(a) Whether the lists are of the same length. 
(b) Whether the elements in each list sum to the same value. 
(c) Whether there are any values that occur in both lists
'''
def compare_lists():
    list1 = list(map(int, input("Enter numbers for list 1 separated by spaces: ").split()))
    list2 = list(map(int, input("Enter numbers for list 2 separated by spaces: ").split()))
    print("Lists have the same length:", len(list1) == len(list2))
    print("Lists sum to the same value:", sum(list1) == sum(list2))
    print("Common values:", set(list1) & set(list2))


compare_lists()
