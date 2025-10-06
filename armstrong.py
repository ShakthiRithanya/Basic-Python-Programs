# Program to check for Armstrong Numbers using custom power and order functions

def power(x, y):
    """
    Calculates x raised to the power of y (x^y) using the standard 
    'Exponentiation by Squaring' method for efficiency.
    """
    # Base case: x^0 is 1
    if y == 0:
        return 1
    
    # Recursive step: Calculate power(x, y//2) only once
    temp = power(x, y // 2)
    
    # If y is even (y = 2k), x^y = (x^k)^2
    if y % 2 == 0:
        return temp * temp
    # If y is odd (y = 2k + 1), x^y = x * (x^k)^2
    else:
        return x * temp * temp
    
def order(x):
    """
    Calculates the number of digits in an integer x.
    """
    n = 0
    # Use a direct string conversion for cleaner digit counting
    # Note: The original while loop is also correct and efficient for integer-only approach.
    if x == 0:
        return 1
    return len(str(abs(x)))
    
    # --- Original logic (commented out but correct) ---
    # while (x != 0):
    #     n = n + 1
    #     x = x // 10
    # return n
    
def isArmstrong(x):
    """
    Checks if a number x is an Armstrong Number.
    An Armstrong number equals the sum of its digits raised to the power of the number of digits.
    """
    # 1. Find the number of digits (n)
    n = order(x)
    temp = x
    sum1 = 0
    
    # 2. Calculate the sum of digits raised to the power n
    while (temp != 0):
        r = temp % 10 # Get the last digit
        sum1 = sum1 + power(r, n)
        temp = temp // 10 # Remove the last digit

    # 3. Compare the sum with the original number
    return (sum1 == x)

# --- Test Cases ---
x = 153
print(f"Is {x} an Armstrong Number? {isArmstrong(x)}")

x = 1253
print(f"Is {x} an Armstrong Number? {isArmstrong(x)}")