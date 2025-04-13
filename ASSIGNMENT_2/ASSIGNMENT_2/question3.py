'''Write a function to check whether the given number is Armstrong or not.'''
def is_armstrong(n):
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return n == sum(d ** power for d in digits)

#giving the number
num = 123
print(f"{num} is an Armstrong number: {is_armstrong(num)}")
