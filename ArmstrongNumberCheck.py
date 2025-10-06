# Program to check if a number is an Armstrong Number (Narcissistic Number)

print("An Armstrong Number is a number which is equal to the sum of its digits raised to the power of the number of digits.")

while True:
    inputNumber_str = input("Enter a positive integer to check: ")
    
    # 1. Input Validation
    if not inputNumber_str.isdigit():
        print("Invalid input. Please enter a whole number.")
        continue
    
    break

# --- Calculation ---

# Get the number of digits, which is the power (n)
power_n = len(inputNumber_str) 
sum_of_powers = 0

# Convert the input string to an integer for final comparison
original_number = int(inputNumber_str)

for digit_char in inputNumber_str:
    # Convert character digit to integer
    digit_val = int(digit_char)
    
    # Raise the digit to the power of n (the total number of digits)
    sum_of_powers += digit_val ** power_n

# --- Result ---

print("-" * 35)

if sum_of_powers == original_number:
    print(f"✅ {original_number} is an Armstrong Number (power: {power_n}).")
else:
    print(f"❌ {original_number} is NOT an Armstrong Number.")