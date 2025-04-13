'''Write a function to check whether the given number is prime or not'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#giving the number
num = 29
print(f"{num} is prime: {is_prime(num)}")