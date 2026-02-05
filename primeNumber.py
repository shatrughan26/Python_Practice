import math 

def is_prime(n):
    """check if a number is prime"""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    limit = int(math.sqrt(number))
    print(limit)
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return False
        
    return True

# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
  