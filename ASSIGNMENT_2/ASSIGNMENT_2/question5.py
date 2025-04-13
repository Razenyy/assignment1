''' Create a program called calculator with functions to perform the following arithmetic calculations, each should take two decimal parameters and return the result of the arithmetic calculation in question.[7]
A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Truncated division
F. Modulus
G. Exponentiation
'''
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else 'Undefined'
def truncated_div(a, b): return a // b if b != 0 else 'Undefined'
def modulus(a, b): return a % b if b != 0 else 'Undefined'
def exponentiate(a, b): return a ** b

#giving the number to do add,subtract,multiply,divide etc. 
print(add(5, 3))           
print(subtract(5, 3))
print(multiply(5, 3))     
print(divide(5, 3))        
print(truncated_div(5, 3)) 
print(modulus(5, 3))       
print(exponentiate(5, 3))  
