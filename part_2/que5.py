'''Write a program to find the simple interest when the value of principle, rate of interest and time period is provided by the user'''
def calculate_simple_interest(principal, rate, time):
    
    simple_interest = (principal * rate * time) / 100
    return simple_interest


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))


simple_interest = calculate_simple_interest(principal, rate, time)
print(f"The simple interest is: {simple_interest:.2f}")